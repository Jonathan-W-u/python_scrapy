import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class Zww2Spider(CrawlSpider):
    name = 'zww2'
    allowed_domains = ['81zw.com']
    # start_urls = ['https://www.81zw.com/book/28463/9813529.html']
    # 因为得不到第一章的数据，所以修改起始页
    start_urls = ['https://www.81zw.com/book/28463/']

    rules = (
        # Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
        # 获取第一章的数据
        Rule(LinkExtractor(restrict_xpaths=r'//div[@id="list"]/dl/dd[1]/a'), callback='parse_item', follow=True),
        # 获取从第二章才开始得到的数据
        Rule(LinkExtractor(restrict_xpaths=r'//div[@class="bottem1"]/a[3]'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        title = response.xpath('//div[@class="bookname"]/h1/text()').extract_first()
        content = ''.join(response.xpath('//div[@id="content"]/text()').extract()).replace('    ','\n')

        yield {
            'title': title,
            'content': content,
        }


        # item = {}
        # #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        # #item['name'] = response.xpath('//div[@id="name"]').get()
        # #item['description'] = response.xpath('//div[@id="description"]').get()
        # return item
