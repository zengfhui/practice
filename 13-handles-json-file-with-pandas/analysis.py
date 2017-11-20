
import json 
import pandas as pd
from pandas import Series,DataFrame

def analysis(file,user_id):
	times = 0
	minutes = 0
	try:
		df = pd.read_json(file)
		df1 = df[df['user_id'] == user_id]
		times = df1['minutes'].count()
		minutes = df1['minutes'].sum()
	except:
		times = 0
		minutes = 0
	return times,minutes


