#!/usr/bin/env python

import scrapy
#from scrapy.pipelines.images import ImagesPipeline
#from scrapy.exceptions import DropItem
from artisan.items import FileItem

class spider_link(scrapy.Spider):
	name = "posts"
	start_urls = [
		'https://old.reddit.com/r/ArtisanMacro/top/?sort=top&t=week',
		'https://old.reddit.com/r/ArtisanMacro/top/?sort=top&t=all',
		'https://old.reddit.com/r/ArtisanMacro/top/?sort=top&t=all&count=25&after=t3_bwcum7',
		'https://old.reddit.com/r/ArtisanMacro/top/?sort=top&t=all&count=50&after=t3_7boneo',
		'https://old.reddit.com/r/ArtisanMacro/top/?sort=top&t=all&count=75&after=t3_8o1o82',
		'https://old.reddit.com/r/ArtisanMacro/top/?sort=top&t=all&count=100&after=t3_b2yfbr'
		]

	def parse(self, response):
		for posts in response.css('div.top-matter'):
                       yield FileItem(
                               title =  posts.css('a::text').get(),
                               author = posts.css('span::text').get(),
                               file_urls =  [posts.css('a').attrib['href']],
                       )
