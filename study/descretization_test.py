# -*- coding: utf-8 -*-
"""
@time:2018/7/15 21:55

@author: BX
"""
import pandas as pd
datafile=r'H:\data_test\chapter4\demo\data\discretization_data.xls'
data=pd.read_excel(datafile)
data=data['肝气郁结证型系数'].copy()
print(type(data))
k=4
d1=pd.cut(data,k,labels=range(k))#等宽离散化，各个类别命名为0,1,2,3
#print(d1)
#print(d1==0)

#等频率离散化
#import math
w=[1.0*i/k for i in range(k+1)]
w=data.describe(percentiles=w)[4:4+k+1]#利用describe函数自动计算分位数
w[0] = w[0]*(1-1e-10)#1的-10次方#确保比最小值小
#print(w)
#print(w[0])
d2=pd.cut(data,w,labels=range(k))
#print(d2)


#聚类离散化
import numpy as np
from sklearn.cluster import KMeans
kmodel=KMeans(n_clusters=k,n_jobs=1)#n_jobs并行数，一般等于CPU数比较好
kmodel.fit(np.array(data).reshape((-1, 1)))#训练模型
c = pd.DataFrame(kmodel.cluster_centers_)
print(c)
w1= pd.rolling_mean(c, 2)
print(w1)
w1= [0] + list(w1[0]) + [data.max()]
d3 = pd.cut(data, w1, labels = range(k))
#print()


def cluster_plot(d,k):
    import matplotlib.pyplot as plt
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.rcParams['axes.unicode_minus']=False

    plt.figure(figsize=(8,3))
    for j in range(0,k):
        plt.plot(data[d==j],[j for i in d[d==j]],'o')
       # print(data[d==j])
    plt.ylim(-0.5,k-0.5)
    return plt
cluster_plot(d1,k).show()
cluster_plot(d2,k).show()
cluster_plot(d3,k).show()