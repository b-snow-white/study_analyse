# -*- coding: utf-8 -*-
"""
@time:2018/7/15 15:08

@author: BX
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# x=np.linspace(0,2*np.pi,50)
# y=np.sin(x)
# plt.plot(x,y,'bp--')#绘制图形格式为蓝色带星虚线
# plt.show()


#饼图
labels='Frogs','Hogs','Dogs','Logs'#定义标签
sizes=[15,35,40,10]
colors=['yellowgreen','gold','lightskyblue','lightcoral']
explode=(0,0.1,0,0)#突出显示第二块explode (每一块)离开中心距离
#autopct控制饼图内百分比设置,shadow  是否阴影
# startangle  起始绘制角度,默认图是从x轴正方向逆时针画起,如设定=90则从y轴正方向画起
plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,startangle=90)
plt.axis('equal')#显示为圆（避免压缩比例成椭圆）
plt.show()

#二维条形直方图
x=np.random.randn(1000)
plt.hist(x,10)

#箱线图
x=np.random.randn(1000)
D=pd.DataFrame([x,x+1]).T
D.plot(kind='box')

#plot(logx=True),绘制x或者Y 的对数图形
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
x=pd.Series(np.exp(np.arange(20)))
x.plot(label='原始数据图',legend=True)
plt.show()
x.plot(logy=True,label='对数数据图',legend=True)
plt.show()

#绘制误差条形图
error=np.random.randn(10)#定义误差列
y=pd.Series(np.sin(np.arange(10)))#均指数据列
y.plot(yerr=error)#绘制误差线
plt.show()
