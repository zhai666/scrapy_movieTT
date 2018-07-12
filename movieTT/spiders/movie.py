# -*- coding: utf-8 -*-
import os

import scrapy

class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['www.dytt8.net/']
    start_urls = ['http://www.dytt8.net/html/gndy/dyzz/']

    def parse(self, response):
        # 解析电影列表
        # list[Selector]
        links = response.xpath('//a[@class="ulink"]')
        for link in links:
            try:

                name = link.xpath('./text()').extract()[0]
                href = link.xpath('./@href').extract()[0]
                print(href)

                # 拼接路径
                # href = response.urljoin(href)
            except:
                pass
            else:
                # print(name,href,sep='\n')
                # 发起详情页面的请求
                # yield scrapy.Request(href,callback=self.parse_video)

                print('--'*30)

    def parse_video(self, response):
        with open('movie_info.html','wb') as f:
            f.write(response.body)
        # 解析详情的电影页面
        title = response.xpath('//h1//font/text()').extract()[0]
        video_url = response.xpath('//div[@class="co_area2"]/div[@class="co_content8"]/ul//table/tbody//a/@href').extract()[0]

        print('-----准备下载----',video_url,sep='\n')

        # 下载video
        # os.system(r'd:\xxx\thunder.exe %s'%video_url)
        yield {
            'title':title,
            'video_url':video_url
        }

        yield scrapy.Request(video_url,callback=self.saveVideo)

    def saveVideo(self,response):
        # 保存视频
        print('---保存视频----------')
        print('url:',response.url)
