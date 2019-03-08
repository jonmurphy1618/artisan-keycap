#!/usr/bin/env python

import scrapy

class spider_link(scrapy.Spider):
	name = "posts"
	start_urls = [
		'https://old.reddit.com/r/ArtisanMacro/top/?sort=top&t=week',
		]

	def parse(self, response):
		for posts in response.css('div.top-matter'):
			yield {
				'title': posts.css('a::text').get(),
				'author': posts.css('span::text').get(),
				#'image':
				'link': posts.css('a').attrib['href'],
			}

# scrapy console
# https://old.reddit.com/r/ArtisanMacro/top/?sort=top&t=week
# response.css("div.top-matter")[0].css("a").attrib['href']
## loop for each [0]++ will return the image url

