from .base import WebCrawlerBase
from invana_bot.extractors.content import CustomContentExtractor, \
    ParagraphsExtractor, TableContentExtractor, HTMLMetaTagExtractor
from invana_bot.extractors.links import PaginationLinkExtractor
import scrapy
from invana_bot.utils.url import get_domain, get_absolute_url
from invana_bot.utils.crawlers import get_crawler_from_list
from urllib.parse import urlparse
from invana_bot.traversals.generic import GenericLinkExtractor

TRAVERSAL_LINK_FROM_FIELD = "link_from_field"
TRAVERSAL_SAME_DOMAIN_FIELD = "same_domain"


class InvanaBotSingleWebCrawler(WebCrawlerBase):
    """
    This is generic spider
    """
    name = "InvanaBotSingleWebCrawler"

    def closed(self, reason):
        print("spider closed with payload:", reason, self.current_crawler.get('cti_id'))

    @staticmethod
    def run_extractor(response=None, extractor=None):
        parser_type = extractor.get("parser_type")
        parser_id = extractor.get("parser_id")
        if parser_type in [None, "CustomContentExtractor"]:
            extractor_object = CustomContentExtractor(response=response, extractor=extractor,
                                                      parser_id=parser_id)
        elif parser_type == "TableContentExtractor":
            extractor_object = TableContentExtractor(response=response, extractor=extractor,
                                                     parser_id=parser_id or "tables")

        elif parser_type == "PaginationLinkExtractor":
            extractor_object = PaginationLinkExtractor(response=response, extractor=extractor,
                                                       parser_id=parser_id or "pagination")

        elif parser_type == "HTMLMetaTagExtractor":
            extractor_object = HTMLMetaTagExtractor(response=response, extractor=extractor,
                                                    parser_id=parser_id or "meta_tags")
        elif parser_type == "ParagraphsExtractor":
            extractor_object = ParagraphsExtractor(response=response, extractor=extractor,
                                                   parser_id=parser_id or "paragraphs")
        else:
            return {}
        data = extractor_object.run()
        return data

    @staticmethod
    def run_traversals(response=None, traversal=None, **kwargs):

        selector_type =  traversal.get("selector_type")
        kwargs = {}
        if selector_type == "css":
            kwargs['restrict_css'] = traversal.get("selector_value")
        elif selector_type == "xpath":
            kwargs['restrict_xpaths'] = traversal.get("selector_value")
        elif selector_type == "css":
            kwargs['restrict_regex'] = traversal.get("selector_value")

        kwargs['allow_domains'] = traversal.get("allow_domains", [])

        return GenericLinkExtractor(**kwargs).extract_links(response=response)

    @staticmethod
    def get_subdocument_key(crawler=None, parser_id=None):
        """
        element is the subdocument key name.

        :param crawler:
        :param parser_id:
        :param selector_id:
        :return:
        """
        for extractor in crawler['parsers']:
            if extractor.get("parser_id") == parser_id:
                for selector in extractor.get('data_selectors', []):
                    if selector.get('selector_attribute') == 'element':
                        return selector.get("selector_id")
        return

    def post_parse(self, response=None):
        pass

    def parse_error(self, failure):
        pass

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(
                url,
                callback=self.parse,
                errback=self.parse_error,
                dont_filter=True,
                meta={
                    "current_page_count": 0,
                    "current_crawler": self.current_crawler,
                    "crawlers": self.crawlers
                }
            )

    def parse(self, response=None):

        current_crawler = response.meta.get("current_crawler")
        crawlers = response.meta.get("crawlers")
        context = self.context

        if None in [crawlers, current_crawler]:
            current_crawler = self.current_crawler
            crawlers = self.crawlers

        data = {}
        for extractor in current_crawler['parsers']:
            extracted_data = self.run_extractor(response=response, extractor=extractor)
            data.update(extracted_data)

        if context is not None:
            data.update({"context": context})
        data['url'] = response.url
        data['domain'] = get_domain(response.url)
        data['context']['crawler_id'] = current_crawler['crawler_id']
        yield data

        for traversal in current_crawler.get('traversals', []):
            traversal['allow_domains'] = current_crawler.get("allowed_domains", [])
            traversal_id = traversal['traversal_id']
            # print("traversal=====", traversal)
            traversal_links = self.run_traversals(response=response, traversal=traversal)
            print("=================================================")
            print("====traversal_links", traversal_id, len(traversal_links))
            print("=================================================")
            next_crawler_id = traversal['next_crawler_id']
            next_crawler = get_crawler_from_list(crawler_id=next_crawler_id, crawlers=crawlers)
            for link in traversal_links:
                current_page_count = response.meta.get('current_page_count', 1)

                yield scrapy.Request(
                    link,
                    callback=self.parse,
                    errback=self.parse_error,

                    meta={
                        "current_page_count": current_page_count,
                        "current_crawler": next_crawler,
                        "crawlers": crawlers,
                    }
                )

            # if traversal['traversal_type'] == "pagination":
            #     # TODO - move this to run_pagination_traversal(self, response=None, traversal=None) method;
            #     traversal_config = traversal['pagination']
            #     next_crawler_id = traversal['next_crawler_id']
            #     max_pages = traversal_config.get("max_pages", 1)
            #     if current_page_count < max_pages:
            #         next_selector = traversal_config.get('selector')
            #         if next_selector:
            #             if traversal_config.get('selector_type') == 'css':
            #                 next_page = response.css(next_selector + "::attr(href)").extract_first()
            #             elif traversal_config.get('selector_type') == 'xpath':
            #                 next_page = response.xpath(next_selector + "::attr(href)").extract_first()
            #             else:
            #                 next_page = None
            #             current_page_count = current_page_count + 1
            #             if next_page:
            #                 if not "://" in next_page:
            #                     next_page_url = "https://" + get_domain(response.url) + next_page
            #                 else:
            #                     next_page_url = next_page
            #                 next_crawler = get_crawler_from_list(crawler_id=next_crawler_id, crawlers=crawlers)
            #                 yield scrapy.Request(
            #                     next_page_url,
            #                     callback=self.parse,
            #                     errback=self.parse_error,
            #
            #                     meta={
            #                         "current_page_count": current_page_count,
            #                         "current_crawler": next_crawler,
            #                         "crawlers": crawlers,
            #                     }
            #                 )
            # elif traversal['traversal_type'] == TRAVERSAL_LINK_FROM_FIELD:
            #     next_crawler_id = traversal['next_crawler_id']
            #     traversal_config = traversal[TRAVERSAL_LINK_FROM_FIELD]
            #
            #     subdocument_key = self.get_subdocument_key(
            #         crawler=current_crawler,
            #         parser_id=traversal_config['parser_id']
            #     )
            #
            #     for item in data.get(traversal_config['parser_id']).get(subdocument_key, []):
            #         traversal_url = item[traversal[TRAVERSAL_LINK_FROM_FIELD]['selector_id']]
            #         if traversal_url:
            #             if "://" not in traversal_url:  # TODO - fix this monkey patch
            #                 url_parsed = urlparse(response.url)
            #                 traversal_url = url_parsed.scheme + "://" + url_parsed.netloc + "/" + traversal_url.lstrip(
            #                     "/")
            #
            #             next_crawler = get_crawler_from_list(crawler_id=next_crawler_id, crawlers=crawlers)
            #             yield scrapy.Request(
            #                 traversal_url,
            #                 callback=self.parse,
            #                 errback=self.parse_error,
            #
            #                 meta={
            #                     "crawlers": crawlers,
            #                     "current_crawler": next_crawler,
            #                 }
            #             )
            #         else:
            #             print("ignoring traversal to {}".format(traversal_url))
            # elif traversal['traversal_type'] == TRAVERSAL_SAME_DOMAIN_FIELD:
            #     all_urls = response.css("a::attr(href)").extract()
            #     filtered_urls = []
            #     all_urls = list(set(all_urls))
            #     current_domain = get_domain(response.url)
            #     for url in all_urls:
            #         url = get_absolute_url(url=url, origin_url=response.url)
            #         if get_domain(url) == current_domain:
            #             filtered_urls.append(url)
            #     filtered_urls = list(set(filtered_urls))
            #     # max_pages = traversal.get("max_pages", 100)
            #     #  implementing max_pages is difficult cos it keeps adding
            #     # new 100 pages in each thread.
            #     current_page_count = response.meta.get('current_page_count', 1)
            #     next_crawler_id = traversal['next_crawler_id']
            #     next_crawler = get_crawler_from_list(crawler_id=next_crawler_id, crawlers=crawlers)
            #
            #     for url in filtered_urls:
            #         current_page_count = current_page_count + 1
            #
            #         yield scrapy.Request(
            #             url, callback=self.parse,
            #             errback=self.parse_error,
            #
            #             meta={
            #                 "current_page_count": current_page_count,
            #                 "current_crawler": next_crawler,
            #                 "crawlers": crawlers
            #             }
            #         )
        self.post_parse(response=response)
