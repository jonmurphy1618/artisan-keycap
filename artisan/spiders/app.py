#!/usr/bin/env python

import scrapy
#from scrapy.pipelines.images import ImagesPipeline
#from scrapy.exceptions import DropItem
from artisan.items import FileItem

class spider_link(scrapy.Spider):
	name = "posts"
	start_urls = [
		'https://old.reddit.com/r/ArtisanMacro/top/?sort=top&t=week',
		]

	def parse(self, response):
		for posts in response.css('div.top-matter'):
			#img_url = 'https://i.redd.it/4wy452iuj7q21.jpg'
#			img_url = posts.css('a').attrib['href']
#			yield FileItem(file_urls=[img_url])

#			yield {
#				'title': posts.css('a::text').get(),
#				'author': posts.css('span::text').get(),
#				'file_urls': FileItem(posts.css('a').attrib['href']),
#				'link': posts.css('a').attrib['href'],
#			}

                       yield FileItem(
                               title =  posts.css('a::text').get(),
                               author = posts.css('span::text').get(),
                               file_urls =  [posts.css('a').attrib['href']],
                       )









#class MyImagesPipeline(ImagesPipeline):
#	def get_media_requests(self, item, info):
#		for image_url in item['image_urls']:
#			yield scrapy.Request(image_url)
#
#	def item_completed(self, results, item, info):
#		image_paths = [x['path'] for ok, x in results if ok]
#		if not image_paths:
#			raise DropItem("Item contains no images")
#		item['image_paths'] = image_paths
#		return item

# scrapy console
# https://old.reddit.com/r/ArtisanMacro/top/?sort=top&t=week
# response.css("div.top-matter")[0].css("a").attrib['href']
## loop for each [0]++ will return the image url

