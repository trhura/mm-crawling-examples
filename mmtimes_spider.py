from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from helper import *
import scrapy.log
from urlparse import urlparse
from myanmar import converter

class VoiceSpider (CrawlSpider):
    name = "mmtimes_spider"
    allowed_domains = ["myanmar.mmtimes.com"]
    start_urls = [
        "http://www.myanmar.mmtimes.com/",
        "http://www.myanmar.mmtimes.com/mtm452.html",
        "http://www.myanmar.mmtimes.com/mtm453.html",
        "http://www.myanmar.mmtimes.com/mtm454.html",
        "http://www.myanmar.mmtimes.com/mtm455.html",
        "http://www.myanmar.mmtimes.com/mtm456.html",
        "http://www.myanmar.mmtimes.com/mtm457.html",
        "http://www.myanmar.mmtimes.com/mtm458.html",
        "http://www.myanmar.mmtimes.com/mtm459.html",
        "http://www.myanmar.mmtimes.com/mtm460.html",
        "http://www.myanmar.mmtimes.com/mtm461.html",
        "http://www.myanmar.mmtimes.com/mtm462.html",
        "http://www.myanmar.mmtimes.com/mtm463.html",
        "http://www.myanmar.mmtimes.com/mtm464.html",
        "http://www.myanmar.mmtimes.com/mtm465.html",
        "http://www.myanmar.mmtimes.com/mtm466.html",
        "http://www.myanmar.mmtimes.com/mtm467.html",
        "http://www.myanmar.mmtimes.com/mtm468.html",
        "http://www.myanmar.mmtimes.com/mtm469.html",
        "http://www.myanmar.mmtimes.com/mtm470.html",
        "http://www.myanmar.mmtimes.com/mtm471.html",
        "http://www.myanmar.mmtimes.com/mtm472.html",
        "http://www.myanmar.mmtimes.com/mtm473.html",
        "http://www.myanmar.mmtimes.com/mtm474.html",
        "http://www.myanmar.mmtimes.com/mtm475.html",
        "http://www.myanmar.mmtimes.com/mtm476.html",
        "http://www.myanmar.mmtimes.com/mtm477.html",
        "http://www.myanmar.mmtimes.com/mtm478.html",
        "http://www.myanmar.mmtimes.com/mtm479.html",
        "http://www.myanmar.mmtimes.com/mtm480.html",
        "http://www.myanmar.mmtimes.com/mtm481.html",
        "http://www.myanmar.mmtimes.com/mtm482.html",
        "http://www.myanmar.mmtimes.com/mtm483.html",
        "http://www.myanmar.mmtimes.com/mtm484.html",
        "http://www.myanmar.mmtimes.com/mtm485.html",
        "http://www.myanmar.mmtimes.com/mtm486.html",
        "http://www.myanmar.mmtimes.com/mtm487.html",
        "http://www.myanmar.mmtimes.com/mtm488.html",
        "http://www.myanmar.mmtimes.com/mtm489.html",
        "http://www.myanmar.mmtimes.com/mtm490.html",
        "http://www.myanmar.mmtimes.com/mtm491.html",
        "http://www.myanmar.mmtimes.com/mtm492.html",
        "http://www.myanmar.mmtimes.com/mtm493.html",
        "http://www.myanmar.mmtimes.com/mtm494.html",
        "http://www.myanmar.mmtimes.com/mtm495.html",
        "http://www.myanmar.mmtimes.com/mtm496.html",
        "http://www.myanmar.mmtimes.com/mtm497.html",
        "http://www.myanmar.mmtimes.com/mtm498.html",
        "http://www.myanmar.mmtimes.com/mtm499.html",
        "http://www.myanmar.mmtimes.com/mtm500.html",
        "http://www.myanmar.mmtimes.com/mtm501.html",
        "http://www.myanmar.mmtimes.com/mtm502.html",
        "http://www.myanmar.mmtimes.com/mtm503.html",
        "http://www.myanmar.mmtimes.com/mtm504.html",
        "http://www.myanmar.mmtimes.com/mtm505.html",
        "http://www.myanmar.mmtimes.com/mtm506.html",
        "http://www.myanmar.mmtimes.com/mtm507.html",
        "http://www.myanmar.mmtimes.com/mtm508.html"
    ]
    manager = ItemManager (name)
    rules = (
        Rule (SgmlLinkExtractor (), callback='parse_item', follow=True),
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