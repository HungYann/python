# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from xiaoshuo.items import XiaoshuoItem


class XiaoshuoSpiderSpider(CrawlSpider):
    name = 'xiaoshuo_spider'
    allowed_domains = ['www.zwdu.com']
    start_urls = ['https://www.zwdu.com/book/25435/7774879.html']

    rules = (
        Rule(LinkExtractor(allow=r'https://www.zwdu.com/book/25435/.+.html'), callback='parse_item', follow=True),

    )



    def parse_item(self, response):


        bookname = response.xpath(".//div[@class='bookname']//text()").getall();

        content=response.xpath(".//div[@id='content']/text()").getall()

        bookname = "".join(bookname).strip()
        content = "".join(content).strip()

        item =  XiaoshuoItem(bookname=bookname,content=content)
        yield item
