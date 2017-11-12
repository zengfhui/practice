# -*- coding: utf-8 -*-
import scrapy
from sylgithub.items import RepositoryItem


class RepositorySpider(scrapy.Spider):
	name = 'repositories'
	
	@property
	def start_urls(self):
		url1_tmp1 = 'https://github.com/shiyanlou?page={}&tab=repositories'
		return (url1_tmp1.format(i) for i in range(1,5))
	
	def parse(self, response):
		for repository in response.css('li.public'):
			item = RepositoryItem({
				'name': repository.xpath('.//a[@itemprop="name codeRepository"]/text()').re_first("\n\s*(.*)"),
				'update_time': repository.xpath('.//relative-time/@datetime').extract_first()
			})
			yield item


        
