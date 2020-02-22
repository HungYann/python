# -*- coding: utf-8 -*-
import scrapy
# https://www.zwdu.com/book/25435/7774888.html
from scrapy.http.response.html import HtmlResponse
from tutorial.items import TutorialItem

class TutorialSpiderSpider(scrapy.Spider):
    name = 'tutorial_spider'
    allowed_domains = ['https://www.zwdu.com/book/25435/7774879.html']
    start_urls = ['https://www.zwdu.com/book/25435/7774879.html']

    def parse(self, response):
        wrappers = response.xpath("//div[@id='wrapper']/div");
        for wrapper in wrappers:

            bookname = wrapper.xpath(".//div[@class='bookname']//text()").getall();
            bookname = "".join(bookname).strip();


            content = wrapper.xpath(".//div[@id='content']//text()").getall();
            content = "".join(content).strip();

            item = TutorialItem(bookname=bookname,content=content)

            # xiaoshuo = {"bookname":bookname,"content":content}
            yield item
