# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html


from scrapy import Field,Item

class BaidubaikeItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field();
    desc = Field();

class BaidubaikeUrl(Item):
    url_link = Field();
    url_type = Field();
    url_desc = Field();