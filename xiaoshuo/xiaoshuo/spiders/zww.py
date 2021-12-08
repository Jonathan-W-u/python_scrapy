import scrapy


class ZwwSpider(scrapy.Spider):
    name = 'zww'
    allowed_domains = ['81zw.com']
    start_urls = ['https://www.81zw.com/book/42206/18321199.html']

    def parse(self, response):
        title = response.xpath('//*[@class="bookname"]/h1/text()').extract_first()
        content = ''.join(response.xpath('//div[@id="content"]/text()').extract()).replace('\xa0\xa0\xa0\xa0','\n')

        yield {
            'title': title,
            'content': content
        }
        next_url = response.xpath('//div[@class="bottem2"]/a[3]/@href').extract()[0]
        # print('next_url:',next_url)

        # 判断是否到了最后一章，如果到了就不执行了
        if next_url.find('.html') != -1:
            base_url = 'https://www.81zw.com{}'.format(next_url)
            yield scrapy.Request(base_url, callback = self.parse)
            # yield scrapy.Request(response.joinurl(next_url), callback = self.parse)

