import scrapy


class ZolSpider(scrapy.Spider):
    name = 'zol'
    allowed_domains = ['zol.com.cn']
    start_urls = ['https://desk.zol.com.cn/bizhi/9834_118409_2.html']

    def parse(self, response):
        image_urls = response.xpath('//img[@id="bigImg"]/@src').extract()
        image_name = response.xpath('string(//div[@class="wrapper photo-tit clearfix"]/h3)').extract_first()
        print(image_urls)
        yield {
            'image_urls': image_urls,
            'image_name': image_name
        }

        # 获取下一张图片
        next_url = response.xpath('//a[@id="pageNext"]/@href').extract_first()

        # 判断是否是最后一张图片
        if next_url.find('.html') != -1:
            yield scrapy.Request(response.urljoin(next_url), callback= self.parse)
