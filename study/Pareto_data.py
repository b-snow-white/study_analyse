# -*- coding: utf-8 -*-
"""
@time:2018/7/13 21:29

@author: BX
"""
import pandas as pd
#初始化数据
dish_profit=r'H:\data_test\chapter3\demo\data\catering_dish_profit.xls'#餐饮菜品盈利数据
data=pd.read_excel(dish_profit,index_col='菜品名')
data=data['盈利'].copy()
print(data)
data.sort_values(ascending=False)
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
plt.figure()
data.plot(kind='bar')#默认为line
plt.ylabel('盈利(元)')
p=1.0*data.cumsum()/data.sum()
print(p)
print(type(p))
p.plot(color='r',secondary_y=True,style='-o',linewidth=2)#secondary_y设置第二个y轴
plt.ylabel('盈利（比例）')
plt.annotate(format(p[6],'.4%'),xy=(6,p[6]),xytext=(6*0.9,p[6]*0.9)
             ,arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=4'))#增加带箭头的注释

plt.show()