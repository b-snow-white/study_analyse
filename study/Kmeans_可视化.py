# -*- coding: utf-8 -*-
"""
@time:2018/7/22 18:25

@author: BX
"""
import pandas as pd
inputfile=r'H:\data_test\chapter5\demo\data\consumption_data.xls'
outputfile=r'H:\data_test\chapter5\demo\tmp\data_types.xls'
k=3
interation=500
data=pd.read_excel(inputfile,index_col='Id')
data_zs=1.0*(data-data.mean())/data.std()#数据标准化
from sklearn.manifold import TSNE
tsne=TSNE()
tsne.fit_transform(data_zs)#进行数据降维
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
#不同类别用不同样式绘图
d=tsne[r]











