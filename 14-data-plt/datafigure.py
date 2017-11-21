#-*-coding:utf-8-*-
import json
import pandas as pd 
from pandas import Series,DataFrame
import matplotlib.pyplot as plt

df = pd.read_json('user_study.json')
data = df.groupby('user_id').sum().sample(15)
#sample(15） 随机选择15个数据
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_xlabel('User ID')
ax.set_ylabel('Study Time')
ax.set_title('StudyData')
ax.plot(data.index,data.minutes)
plt.show()
