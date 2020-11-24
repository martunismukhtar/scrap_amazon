# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonItem(scrapy.Item):
    judul = scrapy.Field()
    link = scrapy.Field()
    tanggal = scrapy.Field()
    imagelink = scrapy.Field()
    pass
