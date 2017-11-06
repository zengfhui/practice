# -*- coding: utf-8 -*-
import scrapy
from shiyanlou.items import UserItem


class UsersSpider(scrapy.Spider):
	name = 'users'
	start_urls = ['https://shiyanlou.com/']
	@property 
	def start_urls(self):
		url_tmp1 = 'https://www.shiyanlou.com/user/{}/'
		return (url_tmp1.format(i) for i in range(525000,524800,-10))

	def parse(self,response):
		item = UserItem({
			'name': response.css('span.username::text').extract(),
			'type': response.css('a.member-icon img.user-icon::attr(title)').extract_first(default = 'normal user'),
			'join_date': response.css('span.join-date::text').extract_first(),
			'level': response.css('span.user-level::text').extract_first(),
			'learn_course_num': response.css('span.latest-learn-num::text').extract_first()
			})
		yield item
