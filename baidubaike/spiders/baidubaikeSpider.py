from scrapy import Spider,Request;
from  baidubaike.items import BaidubaikeItem;
import json;

class BaidubaikeSpider(Spider):
    name = "baidubaike";
    allowed_domains = ['baike.baidu.com'];
    start_urls = ['http://baike.baidu.com'];
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.3',
        'Referer': 'https://item.taobao.com/item.htm',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Connection': 'keep-alive',
    };

    # def start_requests(self):
    #     yield Request(url= 'http://zhihu.com/',headers = self.headers,callback=self.parse());

    def parse(self, response):
        # item = BaidubaikeItem();
        # title = response
        # item['title'] = title;
        # print("This title:"+title);
        # print(response.text);
        return "abc";