# -*- coding: utf-8 -*-
"""
@time:2018/7/15 17:56

@author: BX
"""
from scipy.interpolate import lagrange
import pandas as pd

inputfile=r'H:\data_test\chapter4\demo\data\catering_sale.xls'
outputfile=r'H:\result2.xls'

data=pd.read_excel(inputfile)
data['销量'][(data['销量']<400)|(data['销量']>5000)]=None#过滤异常值，让其变成空值
#print(data)
#print(type(data.columns))
#自定义列向量插值函数
def ployinterp_column(s,n,k=5):
    y=s[list(range(n-k,n))+list(range(n+1,n+1+k))]
    y=y[y.notnull()]#剔除空值
    print(y)
    print(y.index)
    return lagrange(y.index,list(y))(n)#插值并返回插值结果
#逐个元素判断是否需要插值

for i in data.columns:
    for j in range(len(data)):
        if (data[i].isnull())[j]:#空值进行插入
            data[i][j]=ployinterp_column(data[i],j)
data.to_excel(outputfile)