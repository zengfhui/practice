#-*- coding:utf-8 -*-
import os
import json
from flask import Flask 

def create_app():

	app = Flask('rmon')

	ConfigFile = os.environ.get('RMON_CONFIG')
	with open(ConfigFile) as f:
		d_config = json.loads(f.read())
	for key,value in d_config.items():
		app.config[key] = value
	print('yes')
	return app





