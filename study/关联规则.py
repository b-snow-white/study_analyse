# -*- coding: utf-8 -*-
"""
@time:2018/7/23 10:46

@author: BX
"""
from __future__ import print_function
from _Apriori import *
import pandas as pd
inputfile=r'H:\data_test\chapter5\demo\data\menu_orders.xls'
outputfile=r'H:\data_test\chapter5\demo\data\Apriori_rules.xls'

data=pd.read_excel(inputfile,header=None)
print(data)
print('\n转换原始数据至0-1矩阵')
print(pd.Series(1,data.as_matrix()[pd.notnull(data.as_matrix())]))
ct=lambda x:pd.Series(1,index=x[pd.notnull(x)])
b=map(ct,data.as_matrix())
#print(list(b))
data=pd.DataFrame(list(b)).fillna(0)
print(data)
print('转换完毕')
del b
support=0.2
confidence=0.5
ms='---'
find_rule(data,support,confidence,ms).to_excel(outputfile)
