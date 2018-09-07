# -*- coding: utf-8 -*-
"""
@time:2018/7/13 16:42

@author: BX
"""
#使用箱线图检测异常值
import pandas as pd
catering_sale='H:\data_test\chapter3\demo\data\catering_sale.xls'#餐饮数据
data=pd.read_excel(catering_sale,index_col='日期')#读取数据，指定日期列为索引列
print(data.describe())#对数据进行描述性分析结合len(data)
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']#用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False#用来正常显示负号
plt.figure()#建立图像用DataFrame方法
p=data.boxplot(return_type = 'dict')#p为字典类型，其中包含fliers异常值标签
#print(p)
x=p['fliers'][0].get_xdata()#fliers为异常值的标签
#print(x)
y=p['fliers'][0].get_ydata()
#print(y)
y.sort()#从小到大排序该方法直接改变原对象


"""
用annotate添加注释
其中有相似的点，注释会出现重叠，难以看清，所以需要对
xytest【注释内容的坐标点】进行调整
"""
for i in range(len(y)):
    if i>0:
        plt.annotate(y[i],xy=(x[i],y[i]),xytext=(x[i]+0.05 -0.8/(y[i]-y[i-1]),y[i]))
    else:
        plt.annotate(y[i],xy=(x[i],y[i]),xytext=(x[i]+0.08,y[i]))

plt.show()





