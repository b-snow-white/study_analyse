# -*- coding: utf-8 -*-
"""
@time:2018/7/22 11:24

@author: BX
"""
import pandas as pd
inputfile=r'H:\data_test\chapter5\demo\data\consumption_data.xls'
outputfile=r'H:\data_test\chapter5\demo\tmp\data_types.xls'
k=3
interation=500
data=pd.read_excel(inputfile,index_col='Id')
data_zs=1.0*(data-data.mean())/data.std()#数据标准化
from sklearn.cluster import KMeans
model=KMeans(n_clusters=k,n_jobs=1,max_iter=interation)
model.fit(data_zs)#开始聚类
#简单打印结果
r1=pd.Series(model.labels_).value_counts()#统计各个类别的数目
r2=pd.DataFrame(model.cluster_centers_)#找出聚类中心
r=pd.concat([r2,r1],axis=1)#横向连接，得到聚类中心对应的类别下的数目
r.columns=list(data.columns)+["类别数目"]#重命名表头

#print(r)

#详细输出原始数据及其类别
r=pd.concat([data,pd.Series(model.labels_,index=data.index)],axis=1)#详细输出每个样本对应的类别
r.columns=list(data.columns)+['聚类类别']
#r.to_excel(outputfile)
#print(r)
inputfile1=r'H:\data_test\chapter5\demo\tmp\data_types.xls'
data1=pd.read_excel(inputfile1,index_col='Id')
#绘制概率密度图
#import matplotlib.pyplot as plt
#k=3

#聚类类别各属性的密度函数
def density_plot(data,title):
        plt.figure(figsize=(10,8))
        plt.rcParams['font.sans-serif']=['SimHei']#用来正常显示中文标签
        plt.rcParams['axes.unicode_minus']=False#用了来正常显示负号
        plt.figure()
        for i in range(len(data.iloc[0])-1):#逐列做图
            (data.iloc[:,i]).plot(kind='kde',label=data.columns[i],linewidth=2)
        plt.ylabel('密度')
        plt.xlabel('人数')
        plt.title('聚类类别%s各属性的密度曲线'%title)
        plt.legend()
        return plt
#分群后的密度图
def dednsity_plot1(data):#定义作图函数
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用了来正常显示负号
    p=data.plot(kind='kde',linewidth=2,subplots=True,sharex=False)
    [p[i].set_ylabel('密度') for i in range(k)]
    plt.legend()
    return plt
# pic_output=r'H:\data_test\chapter5\demo\tmp\pd_'
# for i in range(k):
#     dednsity_plot1(data[r['聚类类别']==i]).savefig('%s%s.png'%(pic_output,i))
#print(data[r['聚类类别']==1])

from sklearn.manifold import TSNE
tsne=TSNE()
a=tsne.fit_transform(data_zs)#进行数据降维
print(len(a))
tsne=pd.DataFrame(tsne.embedding_,index=data_zs.index)
print(type(tsne))
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
plt.figure()
#不同类别用不同样式绘图
#print(data[r['聚类类别']==0])
d=tsne[r['聚类类别']==0]
plt.plot(d[0],d[1],'r.')
d=tsne[r['聚类类别']==1]
plt.plot(d[0],d[1],'go')
d=tsne[r['聚类类别']==2]
plt.plot(d[0],d[1],'b*')
plt.show()


