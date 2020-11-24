from scrapy import signals
from scrapy import Spider
# from scrapy import signals
# import scrapy.downloadermiddlewares.useragent
from ..items import AmazonItem

import dateparser

class AmazonSpider(Spider):
    name = 'amazon'
    start_urls =[
        'https://www.amazon.com/s?i=specialty-aps&bbn=4954955011&rh=n%3A4954955011%2Cn%3A%212617942011%2Cn%3A12899091&ref=nav_em__nav_desktop_sa_intl_sewing_0_2_8_12'
    ]

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(AmazonSpider, cls).from_crawler(crawler, *args, **kwargs)
        # crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
        crawler.signals.connect(spider.item_scraped, signal=signals.item_scraped)
        return spider

    def item_scraped(self, item):
        return item

    def parse(self, response):
        # print(response)
        mainDiv = response.css('div.s-main-slot>div.s-result-item>div.sg-col-inner>span.celwidget>div.s-expand-height>div.a-section>span.rush-component::text').extract()
        print(mainDiv)
        pass

    def spider_closed(self, spider):
        spider.logger.info('Spider sdsdsd closed: %s', spider.name)

#>div.sg-col-inner>div.a-spacing-medium
    # def parse(self, response):
    #     mainDiv = response.css('div.s-main-slot>div.s-result-item>div.sg-col-inner>>span.s-expand-height').extract()
    #     # yield mainDiv
    #     print(mainDiv)