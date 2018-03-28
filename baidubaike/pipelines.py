# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymssql;

class BaidubaikePipeline(object):
    def process_item(self, item, spider):
        print(item,'----------------------\n',spider)
        return item

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

    def process_item(self,items,spider):
        print(items, '----------------------\n', spider)
        ##cursor = self.conn.cursor()
        ##cursor.execute("insert into zhihuUser(remark) values(" + dict(item) + ");");
        return items;

