# -*- coding: utf-8 -*-
"""
@time:2018/7/20 10:54

@author: BX
"""
'逻辑回归针对的是数值型的数据'
import pandas as pd

#参数初始化
filename=r'H:\data_test\chapter5\demo\data\bankloan.xls'
data=pd.read_excel(filename)
x=data.iloc[:,:8].as_matrix()#做为矩阵使用
y=data.iloc[:,8].as_matrix()
from sklearn.feature_selection import RFE#递归特征消除
from sklearn.feature_selection import f_regression as F#通过F检验给出特征值
from sklearn.linear_model import LogisticRegression as LR
from sklearn.linear_model import RandomizedLogisticRegression as RLR#随机逻辑回归进行特征筛选
rlr=RLR()
rlr1=F(x,y)
print(rlr1)#通过F检验得出的特征结果

rlr.fit(x,y)#训练模型
print(rlr.get_support())#获取特征筛选结果
print(rlr.scores_)#.scores_方法获取各个特征的分数
print('通过随机逻辑回归模型筛选特征结束')
print('有效特征：%s'%','.join(data.iloc[:,:8].columns[rlr.get_support()]))
x=data[data.iloc[:,:8].columns[rlr.get_support()]].as_matrix()#筛选好特征
lr=LR()#建立逻辑回归模型
lr.fit(x,y)#用筛选后的特征进行训练模型
print('逻辑回归模型训练结束')
print('模型的平均正确率：%s'% lr.score(x,y))#给出模型的平均正确率


