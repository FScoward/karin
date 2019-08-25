# -*- coding: utf-8 -*-
import scrapy
from karin.items import KarinItem


class BlogSpider(scrapy.Spider):
    name = 'blog'
    allowed_domains = ['www.keyakizaka46.com']
    start_urls = ['http://www.keyakizaka46.com/s/k46o/diary/detail/19313']

    def parse(self, response: scrapy.http.TextResponse):
        item = KarinItem()
        title = response.xpath('/html/body/div/div/div[1]/div/div/div[1]/article/div[1]/div[2]/h3/text()').get()
        posted_date = response.xpath('/html/body/div/div/div[1]/div/div/div[1]/article/div[3]/ul/li/text()').get()
        item['body'] = "".join(self.getResponseBody(response))
        item['title'] = self.remover(title)
        item['posted_date'] = self.remover(posted_date)
        return item

    def getResponseBody(self, response) -> str:
        body = response.xpath('/html/body/div/div/div[1]/div/div/div[1]/article/div[2]/div/div[2]/div[3]//text()')
        strBody = "".join(body.extract())
        return self.remover(strBody)

    @staticmethod
    def remover(target) -> str:
        return target.replace(u'\xa0', u"").strip().replace(u'\n', u'')

