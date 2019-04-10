# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ArtisanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class FileItem(scrapy.Item):
    file_urls = scrapy.Field()
    files = scrapy.Field()
    author = scrapy.Field()
    title = scrapy.Field()
