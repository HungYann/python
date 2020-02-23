

#### 安装Scrapy框架：



安装ssl以此连接https网站：

```python3
sudo yum install -y openssl-devel
```



查看当前使用的python版本：

```python
import sys
sys.path
```



#### 创建项目和爬虫：



创建一个scrapy项目：

`scrapy startproject [爬虫名字]`

```shell
scrapy startproject tutorial
```

目录结构如下：

![Screenshot 2020-02-21 at 15.41.51](https://tva1.sinaimg.cn/large/0082zybpgy1gc42eri0anj30vi0bw75k.jpg)



进入到项目所在路径，执行命令；

`scrape genspider [爬虫名字] [爬虫域名]`

注意名字不能同项目名称相同。

![image-20200221162254627](https://tva1.sinaimg.cn/large/0082zybpgy1gc43ln1tgtj30vi05ogmm.jpg)



| 项目目录结构  |                                            |
| ------------- | ------------------------------------------ |
| items.py      | 用来存放爬虫爬取下的数据模型。             |
| middleware.py | 用来存放各种中间件文件                     |
| piplines.py   | 用来将items的模型存储到本地磁盘中          |
| settings.py   | 本爬虫的一些配置信息（请求头、ip代理池等） |
| scrapy.cfg    | 项目的配置文件                             |
| spiders包     | 所有爬虫文件                               |



#### Scrapy架构图：

![scrapy_architecture_02](https://tva1.sinaimg.cn/large/0082zybpgy1gc52ksw209j312w0q4myc.jpg)





```python
# -*- coding: utf-8 -*-
import scrapy
# https://www.zwdu.com/book/25435/7774888.html
from scrapy.http.response.html import HtmlResponse

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
            print(bookname)
            print("---")
            print(content)

```



![Screenshot 2020-02-22 at 14.58.56](https://tva1.sinaimg.cn/large/0082zybpgy1gc5fzo4r4cj30qs0eo7er.jpg)



JsonItemExporter和JsonLinesItemExporter

保存json数据时，使用这两个类

保存JSON数据的时候，可以使用泽两个类，让操作变得更简单。

1.`JsonItemExporter`:这个是每次把数据添加到内存中，最后统一写入到磁盘中，好处是，存储的数据是一个满足json规则的数据，坏处是，如果数据较大，那么比较消耗内存。



2.`JsonLinesItemExporter`:这是个没吃调用`export_item`的时候就把这个item存储到硬盘中。坏处是每一个字典是一行，整个文件不是一个满足json格式的文件。好处是处理数据的时候就直接存储到了硬盘中，这样不会消耗内存。



```python
from scrapy.exporters import JsonLinesItemExporter

class TutorialPipeline(object):

    def __init__(self):
        self.fp = open("xiaoshuo.json",'wb');
        self.exporter = JsonLinesItemExporter(self.fp,ensure_ascii=False,encoding="UTF-8");


    def open_spider(self,spider):

        print('爬虫开始！')

    def process_item(self, item, spider):

        self.exporter.export_item(item)
        return item

    def close_spider(self):
        self.fp.close()
        print('爬虫结束')
```





#### CrawSpider实现微信小程序社区

1. 使用scrapy创建工程项目

```python
scrapy startproject wxapp
```



2. 创建crawlspider模版

首先`cd wxapp`进入文件夹，接着执行如如下命令：

```python
scrapy genspider -t crawl wxapp_spdier "www.wxapp-union.com"
```



3. 创建成功后，结构如下

![image-20200223112548736](https://tva1.sinaimg.cn/large/0082zybpgy1gc668mwnafj30ve0eujsz.jpg)



正则表达式：

| 符号 | 表述                                                         |
| ---- | ------------------------------------------------------------ |
| .    | 匹配除“`\r`”“`\n`”之外的任何单个字符。要匹配包括“`\r`”“`\n`”在内的任何字符，请使用像 (.\|\r\|\n) 模式 |
| *    | 匹配前面的子表达式零次或多次。例如，zo*能匹配“`z`”、“`zo`”以及“`zoo`”。*等价于{0,}。 |
| +    | 匹配前面的子表达式一次或多次。例如，“`zo+`”能匹配“`zo`”以及“`zoo`”，但不能匹配“`z`”。+等价于{1,}。 |
| ？   | 匹配前面的子表达式零次或一次。例如，“`do(es)?`”可以匹配“`does`”中的“`do`”和“`does`”。?等价于{0,1}。 |



注意两个问题：

注意allow_domains中不能出错，即不能添加http:也不能添加多余的`/`，否则会出错

```python
allowed_domains = ['www.wxapp-union.com']
```

Rule和LinkExtractor决定了爬虫的方向：

1.allow设置规则的方法：要能够限制在我们使用的URL上面，不要跟其他的URL产生相同的正则表达式。



2.什么情况下使用follow: 如果在爬取页面的时候，需要对当前的url界面进行跟进，那么久设置为True，否则设置为False。



3.什么情况下指定callback：如果这个URL对应的页面，只是为了获取更多的url，并不需要里面的数据，那么不需要指定callback，如果想要获取URL对应页面数据，那么需要指定一个callback。



#### Scrapy shell



1.可以方便我们做一些数据提取的测试代码

2.如果想要执行Scrapy命令，应该先进入Scrapy所在环境

3.如果想要读取某个项目的配置信息，那么应该先进入到这个项目中，再执行`scrapy shell`命令

在文件目录下执行：

```shell
scrapy shell http://www.wxapp-union.com/article-5793-1.html
```



获取标题：

```shell
response.xpath("//h1[@class='ph']/text()").get()   
```



#### 发送POST请求：

有时候我们想要在请求数据的时候发送POST请求，那么这时候需要使用Request的子类FormRequest实现。如果想要在爬虫一开始的时候就发送POST请求，那么需要在爬虫类重写start_request(self)方法，并且不再调用start_urls里的url。



![image-20200223150701761](https://tva1.sinaimg.cn/large/0082zybpgy1gc6cms1kijj31g20aygo6.jpg)





#### 模拟登录人人网



1.想要发送Post请求，那么推荐使用`Scrapy.FormRequst`方法，可以方便的使用表单数据

2.如果想在爬虫一开始的时候发送Post请求，那么应该重写`start_requests`方法

```python
# -*- coding: utf-8 -*-
import scrapy


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://renren.com/']

    def start_requests(self):
        url = "http://www.renren.com/PLogin.do"
        data = {"email":"970138074@qq.com","password":"pythonspider"}

        request = scrapy.FormRequest(url,formdata=data,callback=self.parse_page)

        yield request


    def parse_page(self,response):
        request = scrapy.Request(
            url='http://www.renren.com/880151247/profile',callback=self.parse_profile
        )
        yield request

    def parse_profile(self,response):
        with open('dp.html','w',encoding='UTF-8') as fp:
            fp.write(response.text)

```



#### 实现爬取`八一中文网`小说

```
scrapy startproject xiaoshuo
```



```
cd xiaoshuo 
```



```
scrapy genspider -t crawl xiaoshuo_spider "www.zwdu.com"
```



修改setting.py

```
ROBOTSTXT_OBEY = False
DOWNLOAD_DELAY = 1

DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
  'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'
}

ITEM_PIPELINES = {
   'xiaoshuo.pipelines.XiaoshuoPipeline': 300,
}
```



先来定义items.py

```python
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class XiaoshuoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    bookname = scrapy.Field();
    content = scrapy.Field();
```



编写pipelines.py



```python
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import JsonLinesItemExporter


class XiaoshuoPipeline(object):
    def __init__(self):
        self.fp = open('xiaoshuo.json', 'wb')
        self.exporter = JsonLinesItemExporter(self.fp, ensure_ascii=False, encoding='UTF-8')

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self,spider):
        self.fp.close()
```





编写xiaoshuo_spider.py



```python
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

```



最后编写启动文件 start.py



```python
from scrapy import cmdline


cmdline.execute("scrapy crawl wxapp_spdier".split())
```





#### 生成词云

下载环境



```shell
pip install wordcloud
pip install jieba
```



#### python代码：



```python
filename = "xiaoshuo.json"
with open(filename) as op:
    mytext = op.read()

mytext = " ".join(jieba.cut(mytext))

from wordcloud import WordCloud
wordcloud = WordCloud(font_path="simsun.ttf").generate(mytext)

%pylab inline
import matplotlib.pyplot as plt
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
```



#### 结果如下：

![Screenshot 2020-02-23 at 17.24.54](https://tva1.sinaimg.cn/large/0082zybpgy1gc6h0zsndlj30gs08gwlx.jpg)







#### 学习资源



[Scrapy视频](https://www.bilibili.com/video/av57909837?p=3)

[词云【中】](https://zhuanlan.zhihu.com/p/28954970)

[词云【英】](https://zhuanlan.zhihu.com/p/28948653)