# -*- coding: utf-8 -*-
"""
@time:2018/7/23 18:24

@author: BX
"""
#还有错误
import pandas as pd
#参数初始化
discfile=r'H:\data_test\chapter5\demo\data\arima_data.xls'
forecastnum=5

#读取数据，指定日为指标，Pandas自动将“日期”列识别为Datetime格式
data=pd.read_excel(discfile,index_col='日期')
print(data)
#时序图
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
data.plot()
plt.show()

#自相关图
from statsmodels.graphics.tsaplots import plot_acf
plot_acf(data).show()

#平稳性检验
from statsmodels.tsa.stattools import adfuller as ADF
print('原始序列的ADF检验结果为：',ADF(data['销量']))
#最后一个为p值，判断ｐ值是否显著大于０.０５，如果显著，则为非平稳序列

#差分后的结果　
D_data=data.diff().dropna()
#print(D_data)
D_data.columns=['销量差分']
D_data.plot()#时序图
plt.show()
plot_acf(D_data).show()#自相关图
from statsmodels.graphics.tsaplots import plot_pacf
plot_pacf(D_data).show()#偏自相关图
print('差分序列的ADF检验结果为：',ADF(D_data['销量差分']))#平稳性检验,p<0.05

#白噪声检验，根据p值看出为非白噪声序列(纯随机性数列)
from statsmodels.stats.diagnostic import acorr_ljungbox
print('差分序列的白噪声检验结果为：',acorr_ljungbox(D_data,lags=1))#一阶差分之后的包噪声检验

from statsmodels.tsa.arima_model import ARIMA

#定阶
pmax=int(len(D_data)/10)
qmax=int(len(D_data)/10)
bic_matrix=[]#bic矩阵
for p in range(pmax+1):
    tmp=[]
    for q in range(qmax+1):
        try:#存在部分报错，所以try来跳过报错
            tmp.append(ARIMA(data,(p,1,q)).fit().bic)
            #print(tmp)
        except:
            tmp.append(None)
    bic_matrix.append(tmp)
bic_matrix=pd.DataFrame(bic_matrix)#从中可以找出最小值
print(bic_matrix)
p,q=bic_matrix.stack().idxmin()#先用stack展平，然后idxmin找出最小值位置
print('BIC最小的p值和q值为：%s、%s'%(p,q))
model=ARIMA(data,(p,1,q)).fit()#建立（0,1,1）模型
#print(model.summary2())#给出一份模型报告
print(model.forecast(5))#做为期5天的预测，返回预测结果，标准误差，置信区间

