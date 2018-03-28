# -*- coding: utf-8 -*-
from scrapy import Spider;
from baidubaike.items import BaidubaikeUrl



class BaidubaikeUrlSpider(Spider):
    name = "baidubaikeUrl";
    allow_domains = ['baike.baidu.com'];
    start_urls = ['http://baike.baidu.com'];

    def parse(self, response):
        commonCategories = response.xpath('//*[@id="commonCategories"]/dl/dd/div/a')
        for link in commonCategories:
            item = BaidubaikeUrl();
            item['url_link'] = str(link.select('@href').extract());
            item['url_type'] = 1;
            item['url_desc'] = link.select('text()').extract();
            yield item;




