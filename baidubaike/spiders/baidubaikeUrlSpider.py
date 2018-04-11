# -*- coding: utf-8 -*-
from scrapy import Spider,Request;
from baidubaike.items import BaidubaikeUrl;
from baidubaike.items import BaidubaikeItem;
from baidubaike.public_function import const;
from  baidubaike import public_function;
import re;
import json;


class BaidubaikeUrlSpider(Spider):
    name = "baidubaikeUrl";
    allow_domains = ['baike.baidu.com'];
    start_urls = ['http://baike.baidu.com'];
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.3',
        'Referer': 'https://item.taobao.com/item.htm',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Connection': 'keep-alive',
    };
    index = 1;
    pageSize = 100;
    goTo_Link = "";


    def parse(self, response):
        commonCategories = response.xpath('//*[@id="commonCategories"]/dl/dd/div/a')
        for link in commonCategories:
            var = str(link.xpath('@href').extract()[0]);
            item = BaidubaikeUrl();
            pattern1 =  re.compile(r'^http.*',re.I);
            if pattern1.match(var) != None:
                item['url_link'] = var;
            else:
                item['url_link'] = const.URL +  var;
            #type =1 表示第一级目录
            item['url_type'] = 1;
            item['url_desc'] = link.xpath('text()').extract()[0];
            yield item
            pattern2 = re._compile(r'/[a-zA-Z]+/[\u4E00-\u9FA5]+$', re.I);
            if pattern2.match(var) != None:
                self.goTo_Link = const.URL + var;
                goto_url = public_function.function_parse_url_utf8(const.URL + var+public_function.baidubaike_paging_url(self.pageSize,self.index));
                yield Request(goto_url,headers = self.headers,callback=self.parse_sonUrl);
            break

    def parse_sonUrl(self,response):
        infos = response.xpath('//*[@id="content-main"]/div[3]/div[2]/div[1]/div[3]/div[1]/ul/li');
        if infos is not None and len(infos) >=0:
            for info in infos:
                title = info.xpath('div[@class="list"]/a/text()').extract()[0];
                detail_link = info.xpath('div[@class="list"]/a/@href').extract()[0];
                desc_content = info.xpath('div[@class="list"]/p/text()').extract()[0];
                labels = info.xpath('div[@class="list"]/div[@class="text"]/a');
                labelset ={};
                i = 1;
                for label in labels:
                    labelInfo = label.xpath("text()").extract()[0];
                    labelLink = label.xpath("@href").extract()[0];
                    data = {"labelInfo":labelInfo,"labelLink":const.URL + labelLink}
                    labelset["label"+str(i)] = data;
                    i = i + 1;
                itemInfo = BaidubaikeItem();
                itemInfo['title'] = title;
                itemInfo['label'] = str(dict(labelset));
                itemInfo['desc_content'] = desc_content;
                itemInfo['detail_link'] = const.URL + detail_link;
                yield itemInfo;

            if len(infos) < self.pageSize:
                #本次Url 的循环结束  初始化 参数
                self.index = 1;
                self.goTo_Link = "";
            else:
                self.index = self.index + 1;
                goto_url = public_function.function_parse_url_utf8(self.goTo_Link + public_function.baidubaike_paging_url(self.pageSize, self.index))
                yield Request(goto_url, headers=self.headers, callback=self.parse_sonUrl);
        elif infos is None:
            print("----------------error---------------")



