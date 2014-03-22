from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from helper import *
import scrapy.log
from urlparse import urlparse
from myanmar import converter

class PandoraSpider (CrawlSpider):
    name = "pandora_spider"
    allowed_domains = ["pandora-and-pandora.blogspot.com"]
    start_urls = [
        "http://pandora-and-pandora.blogspot.com"
    ]
    manager = ItemManager (name)
    rules = (
        Rule (SgmlLinkExtractor (), callback='parse_item', follow=True),
        )

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