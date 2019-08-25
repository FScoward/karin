# -*- coding: utf-8 -*-
import scrapy
from karin.items import KarinItem


class BlogSpider(scrapy.Spider):
    name = 'blog'
    allowed_domains = ['www.keyakizaka46.com']
    start_urls = ['http://www.keyakizaka46.com/s/k46o/diary/detail/19313']

    def parse(self, response: scrapy.http.TextResponse):
        item = KarinItem()
        title = response.xpath('/html/body/div/div/div[1]/div/div/div[1]/article/div[1]/div[2]/h3/text()').extract()
        item['body'] = "".join(self.getResponseBody(response))
        item['title'] = "".join(title).replace(u'\xa0', u"").replace(u'\n', u'')
        return item

    def getResponseBody(self, response):
        body = response.xpath('/html/body/div/div/div[1]/div/div/div[1]/article/div[2]/div/div[2]/div[3]//text()')
        strBody = "".join(body.extract()).replace(u'\xa0', u"").replace(u'\n', u'')
        return strBody