#!/usr/bin/env python3

import scrapy

class ShiyanlouCoursesSpoder(scrapy.Spider):
	
	name = 'shiyanlou-courses'

	def start_requests(self):
		url_tmp1 = 'https://www.shiyanlou.com/course/?category=all&course_type=all&fee=all&tag=all&page={}'
		urls = (url_tmp1.format(i) for i in range(1,23))
		for url in urls:
			yield scrapy.Request(url=url,callback=self.parse)

	def parse(self,response):
		for course in response.css('div.course-body'):
			yield{

			'name': course.css('div.course-name::text').extract_first(),
			'descripition': course.css('div.course-desc::text').extract_first(),
			'type': course.css('div.course-footer span.pull-right::text').extract_first(default = 'free'),
			'students': course.xpath('.//span[contains(@class,"pull-left")]/text()[2]').re_first('[^\d]*(\d*)[^\d]*')
			
			}

a = ShiyanlouCoursesSpoder()
filename = '/home/shiyanlou/Code/data.json'
print(a.start_requests())
#with open(filename) as f:
#	f.write(a.start_requests())
			


