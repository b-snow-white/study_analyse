# -*- coding: utf-8 -*-
"""
@time:2018/7/17 14:08

@author: BX
"""
import pandas as pd
inputfile=r'H:\data_test\chapter4\demo\data\principal_component.xls'
outputfile=r'H:\data_test\chapter4\demo\tmp\dimention_reducted.xls'
data=pd.read_excel(inputfile,header=None)
print(data)
from sklearn.decomposition import PCA
pca=PCA()
pca.fit(data)
print(pca.components_)#返回模型的各个特征向量
print(pca.explained_variance_ratio_)#返回各个成分的方差百分比,也称贡献率
#观察方差百分比可以看出提取前三个主成分进行计算
pca=PCA(3)
pca.fit(data)
low_d=pca.transform(data)#降低维度
pd.DataFrame(low_d).to_excel(outputfile)#保存结果
#pca.inverse_transform(low_d)#必要时用Inverse_transform()函数来复原数据

