# -*- coding: utf-8 -*-
import scrapy


class BlogSpider(scrapy.Spider):
    name = 'blog'
    allowed_domains = ['fscoward.karin']
    start_urls = ['http://fscoward.karin/']

    def parse(self, response):
        pass
