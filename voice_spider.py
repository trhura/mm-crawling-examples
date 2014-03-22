from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from helper import *
import scrapy.log
from myanmar import converter
from urlparse import urlparse

class VoiceSpider (CrawlSpider):
    name = "voice_spider"
    allowed_domains = ["thevoicemyanmar.com"]
    start_urls = [
        "http://thevoicemyanmar.com/"
    ]
    manager = ItemManager (name)
    rules = (
        Rule (SgmlLinkExtractor (allow='index\.php'), callback='parse_item',
              follow=True), #process_links='process_links'),
        )

    def process_links (self, response):
        pass

    def parse_item (self, response):
        hxs = HtmlXPathSelector(response)
        paragraphs = hxs.select(r'//p//text()')

        for paragraph in paragraphs:
            paragraph = paragraph.extract ().strip()
            paragraph = converter.convert (paragraph, 'zawgyi','unicode')

            if is_large_paragraph(paragraph) and is_mainly_myanmar(paragraph):
                self.manager.add_item(paragraph)