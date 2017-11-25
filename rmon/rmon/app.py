#-*- coding:utf-8 -*-
"""

此模块主要实现了 app 创建函数，是内层的 app ，外层的 app 是应用的使用入口，调用
此处的 create_app
"""
import os
from flask import Flask
from rmon.views import api
from rmon.models import db
from rmon.config import DevConfig, ProductConfig

def create_app():
	""" 创建并初始化 Flask app
	"""
	app = Flask('rmon')

	#
	env = os.environ.get('RMON_ENV')
	if env in ('pro','prod','product'):
		app.config.from_object(ProductConfig)
	else:
		app.config.from_object(DevConfig)

	app.config.from_envvar('RMON_SETTINGS',silent=True)
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

	#注册 Blueprint
	app.register_blueprint(api)
	#初始化数据库
	db.init_app(app)
	#如果是开发环境则创建所有数据库
	if app.debug:
		with app.app_context():
			db.create_all()
	return app
