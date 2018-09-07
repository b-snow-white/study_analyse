# -*- coding: utf-8 -*-
"""
@time:2018/7/14 14:11

@author: BX
"""

#餐饮销售数据相关性分析
import pandas as pd
catering_sale=r'H:\data_test\chapter3\demo\data\catering_sale_all.xls'
data=pd.read_excel(catering_sale,index_col='日期')
print(type(data))
data.corr()#相关系数矩阵，给出了任意两11q                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    款菜式之间的相关系数
print(type(data.corr()))
print(data.corr()['百合酱蒸凤爪'])#只显示百合与其他菜式的相关系数
print(type(data.corr()['百合酱蒸凤爪']))
print(data['百合酱蒸凤爪'].corr(data['翡翠蒸香茜饺']))#计算两者之间的相关系数