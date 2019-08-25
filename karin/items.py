# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class KarinItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    posted_date = scrapy.Field()
    title = scrapy.Field()
    body = scrapy.Field()
    pass
