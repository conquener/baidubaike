# -*- coding: utf-8 -*-
from scrapy import Spider,Request;
from baidubaike.items import BaidubaikeUrl;
from baidubaike.public_function import const;
from  baidubaike import public_function;
import re;


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


    def parse(self, response):
        commonCategories = response.xpath('//*[@id="commonCategories"]/dl/dd/div/a')
        for link in commonCategories:
            print(link.select('@href'))
            var = str(link.select('@href').extract()[0]);
            item = BaidubaikeUrl();
            pattern1 =  re.compile(r'^http.*',re.I);
            if pattern1.match(var) != None:
                item['url_link'] = var;
            else:
                item['url_link'] = const.URL +  var;
            #type =1 表示第一级目录
            item['url_type'] = 1;
            item['url_desc'] = link.select('text()').extract()[0];
            ##yield item;
            pattern2 = re._compile(r'/[a-zA-Z]+/[\u4E00-\u9FA5]+$', re.I);
            if pattern2.match(var) != None:
                goto_url = public_function.function_parse_url_utf8(const.URL + var+public_function.baidubaike_paging_url(100,1));
                #yield Request(goto_url,headers = self.headers,callback=self.parse_sonUrl);
            break


    def parse_sonUrl(self,response):
        #slider = response.xpath('//*[@id="content-main"]/div[3]/div[2]/div[1]/div[3]/div[1]/ul/li[1]/div[2]/a/text()');

        infos = response.xpath('//*[@id="content-main"]/div[3]/div[2]/div[1]/div[3]/div[1]/ul/li');

        for info in infos:
            title = info.select('div[@class="list"]/a/text()');
            detail_link = info.select('div[@class="list"]/a/@href');
            desc_content = info.select('div[@class="list"]/p/text()');
            labelInfos = info.select('div[@class="list"]/div[@class="text"]/a/text()');
            label = "";
            for labelInfo in labelInfos:
                label = label + labelInfo.extract()[0];
            print(title,title['data'])
            #print(title,'---',detail_link,'---',desc_content,'--',labelInfo,'----',label);

        # file = open('C:\\Users\\Administrator\\Desktop\\baidu.txt','r+',encoding='utf-8');
        # file.write(slider);
        return "";



# 链接 标题   //*[@id="content-main"]/div[3]/div[2]/div[1]/div[3]/div[1]/ul/li/div/a

# 内容  //*[@id="content-main"]/div[3]/div[2]/div[1]/div[3]/div[1]/ul/li[1]/div[2]/p

#开放 分类 标签 //*[@id="content-main"]/div[3]/div[2]/div[1]/div[3]/div[1]/ul/li[1]/div[2]/div/a[1]



