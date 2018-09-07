# -*- coding: utf-8 -*-
"""
@time:2018/7/24 10:28

@author: BX
"""
import pandas as pd
import numpy as np
#参数初始化
inputfile=r'H:\data_test\chapter5\demo\data\consumption_data.xls'
k=3
threshold=2#离群点阀值
iteration=500#聚类最大迭代次数
data=pd.read_excel(inputfile,index_col='Id')
data_zs=1.0*(data-data.mean())/data.std()#数据标准化
from sklearn.cluster import KMeans
model=KMeans(n_clusters=k,n_jobs=1,max_iter=iteration)
model.fit(data_zs)

#标准化数据及其类别
r=pd.concat([data_zs,pd.Series(model.labels_,index=data.index)],axis=1)
r.columns=list(data.columns)+['聚类类别']

norm=[]
for i in range(k):
    norm_tmp=r[['R','F','M']][r['聚类类别']==i]-model.cluster_centers_[i]
    norm_tmp_new=norm_tmp.apply(np.linalg.norm,axis=1)#求出绝对距离
    norm.append(norm_tmp_new/norm_tmp_new.median())#求出并相对距离并添加
norm=pd.concat(norm)#合并
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
norm[norm<=threshold].plot(style='go')#正常点绘图
discrete_point=norm[norm>threshold]#离群点
norm[norm>threshold].plot(style='ro')#离群点绘图

for i in range(len(discrete_point)):
    id=discrete_point.index[i]
    n=discrete_point.iloc[i]
    plt.annotate('(%s,%0.2f)'%(id,n),xy=(id,n),xytext=(id,n))
plt.xlabel('编号')
plt.ylabel('相对距离')
plt.show()






