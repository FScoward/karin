# -*- coding: utf-8 -*-
import scrapy
from karin.items import KarinItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class BlogSpider(CrawlSpider):
    name = 'blog'
    allowed_domains = ['www.keyakizaka46.com']
    start_urls = ['http://www.keyakizaka46.com/s/k46o/diary/detail/19313']

    rules = (
        Rule(LinkExtractor(restrict_xpaths='/html/body/div/div/div[1]/div/div/div[1]/div[1]/div[3]/div[2]/a'),
             callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = KarinItem()
        title = response.xpath('/html/body/div/div/div[1]/div/div/div[1]/article/div[1]/div[2]/h3/text()').get()
        posted_date = response.xpath('/html/body/div/div/div[1]/div/div/div[1]/article/div[3]/ul/li/text()').get()
        item['body'] = "".join(self.getResponseBody(response))
        item['title'] = self.remover(title)
        item['posted_date'] = self.remover(posted_date)
        yield item

    def getResponseBody(self, response) -> str:
        body = response.xpath('/html/body/div/div/div[1]/div/div/div[1]/article/div[2]//text()')
        strBody = "".join(body.extract())
        return self.remover(strBody)

    @staticmethod
    def remover(target) -> str:
        return target.replace(u'\xa0', u"").strip().replace(u'\n', u'')
