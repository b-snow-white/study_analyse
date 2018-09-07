# -*- coding: utf-8 -*-
"""
@time:2018/7/20 16:06

@author: BX
"""
import pandas as pd
filename=r'H:\data_test\chapter5\demo\data\sales_data.xls'
data=pd.read_excel(filename)
#print(data[data=='好'])
data.loc[data['销量']=='高','销量']=int(1)
data.loc[data['销量']=='低','销量']=int(-1)
x=data.iloc[:,1:4].as_matrix()
y=data.iloc[:,4].as_matrix()
print(len(x))
print(len(x[1]))
for i in range(0,len(x)):
    for j in range(0,len(x[i])):
        if (x[i][j]=='是' or x[i][j]=='好'):
            x[i][j]=int(1)
        else:
            x[i][j]=int(-1)
print(data)
from sklearn.tree import DecisionTreeClassifier as DTC
dtc=DTC(criterion='entropy')#建立决策树模型，基于信息熵
dtc.fit(x,y)
#导入相关函数，可视化决策树
from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO
#中文乱码未解决
with open(r'H:\tree.dot','w') as f:
    f=export_graphviz(dtc,feature_names=data.iloc[:,1:4].columns,out_file=f)



