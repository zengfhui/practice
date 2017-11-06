# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ShiyanlouItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class CourseItem(scrapy.Item):
	name = scrapy.Field()
	description = scrapy.Field()
	type = scrapy.Field()
	students = scrapy.Field()

class UserItem(scrapy.Item):

	name = scrapy.Field()
	type = scrapy.Field()
	join_date = scrapy.Field()
	level = scrapy.Field()
	learn_course_num = scrapy.Field()
