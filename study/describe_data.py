# -*- coding: utf-8 -*-
"""
@time:2018/7/13 20:55

@author: BX
"""
import pandas as pd
catering_sale='H:\data_test\chapter3\demo\data\catering_sale.xls'#餐饮数据
data=pd.read_excel(catering_sale,index_col='日期')#读取数据，指定日期列为索引列
data=data[(data['销量']>400)&(data['销量']<5000)]#过滤异常数据
statistics=data.describe()#保存基本统计量
print(type(statistics))
statistics.loc['range']=statistics.loc['max']-statistics.loc['min']#极差
statistics.loc['var']=statistics.loc['std']/statistics.loc['mean']#变异系数
statistics.loc['dis']=statistics.loc['75%']-statistics.loc['25%']#四分位数间距
print(statistics)