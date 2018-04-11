# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymssql;
from baidubaike.items import BaidubaikeItem;
from baidubaike.items import BaidubaikeUrl;

class BaidubaikePipeline(object):
    collect_name = "huangpeng";

    def __init__(self, database_url, database_name, database_user, database_pwd):
        self.database_url = database_url;
        self.database_name = database_name;
        self.database_user = database_user;
        self.database_pwd = database_pwd;

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            database_url=crawler.settings.get('DATABASE_URL'),
            database_name=crawler.settings.get('DATABASE_NAME'),
            database_user=crawler.settings.get('DATABASE_USER'),
            database_pwd=crawler.settings.get('DATABASE_PWD')
        );

    def open_spider(self, spider):
        self.conn = pymssql.connect(self.database_url, self.database_user, self.database_pwd, self.database_name);

    def close_spider(self, spider):
        self.conn.close();

    def process_item(self, item, spider):
        # 插入百科数据 到数据库

        return item;

class BaidubaikeUrlPipeline(object):
    collect_name = "huangpeng";

    def __init__(self,database_url,database_name,database_user,database_pwd):
        self.database_url = database_url;
        self.database_name = database_name;
        self.database_user = database_user;
        self.database_pwd = database_pwd;
    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            database_url = crawler.settings.get('DATABASE_URL'),
            database_name=crawler.settings.get('DATABASE_NAME'),
            database_user = crawler.settings.get('DATABASE_USER'),
            database_pwd = crawler.settings.get('DATABASE_PWD')
        );

    def open_spider(self,spider):
        self.conn = pymssql.connect(self.database_url,self.database_user,self.database_pwd,self.database_name);

    def close_spider(self,spider):
        self.conn.close();

    def process_item(self,item,spider):
        cursor = self.conn.cursor();
        sql = "";
        if isinstance(item,BaidubaikeUrl):
            #插入url 到数据库
            sql = "insert into BAIDUBAIKE_URLS(URL_DESC,URL_LINK,URL_TYPE) values(%s,%s,%d);" ;
            cursor.execute(sql,(item['url_desc'] , item['url_link'] , item['url_type']));
        elif isinstance(item,BaidubaikeItem):
            sql = "insert into BAIDUBAIKE_INFOS(TITLE,DETAIL_LINK,DESC_CONTENT,LABEL) values(%s,%s,%s,%s);" ;
            cursor.execute(sql, (item['title'] , item['detail_link'] , item['desc_content'] , str(item['label'])));

        self.conn.commit();
        return item;

