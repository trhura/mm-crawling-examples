from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
import scrapy.log
from urlparse import urlparse
from myanmar import converter
from helper import *

class MizzimaSpider (CrawlSpider):
    name = "mizzima_spider"
    allowed_domains = ["mizzimaburmese.com"]
    start_urls = [
        "http://www.mizzimaburmese.com",
    ]

    rules = (
        Rule (SgmlLinkExtractor (), callback='parse_item', follow=True),
        )
    manager = ItemManager(name)

    def process_links (self, response):
        pass

    def parse_item (self, response):
        hxs = HtmlXPathSelector(response)
        paragraphs = hxs.select(r"//div//text()")

        for paragraph in paragraphs:
            paragraph = paragraph.extract ().strip()
            paragraph = converter.convert (paragraph, 'zawgyi','unicode')

            if is_large_paragraph(paragraph) and is_mainly_myanmar(paragraph):
                self.manager.add_item(paragraph)
