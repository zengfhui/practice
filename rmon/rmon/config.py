#-*- coding:utf-8 -*-
"""rmon.config

rmon 配置文件
"""
import os
class DevConfig:
	"""开发环境配置
	"""
	DEBUG = True
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	#使用内存数据库？
	SQLALCHEMY_DATABASE_URI = 'sqlite://'
	#自动更新模板文件
	TEMPLATES_AUTO_RELOAD = True

class ProductConfig(DevConfig):
	"""生产环境配置
	"""
	DEBUG = False

	#sqlite 数据库文件路径
	path = os.path.join(os.getcwd(),'rmon.db').replace('\\','/')
	SQLALCHEMY_DATABASE_URI = 'sqlite:///%s' % path
	
