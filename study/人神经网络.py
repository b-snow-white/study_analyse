# -*- coding: utf-8 -*-
"""
@time:2018/7/20 18:41

@author: BX
"""
import pandas as pd
inputfile=r'H:\data_test\chapter5\demo\data\sales_data.xls'
data=pd.read_excel(inputfile,index_col='序号')
data[data=='好']=int(1)
data[data=='高']=int(1)
data[data=='是']=int(1)
data[data!=1]=int(0)
#print(data)
x=data.iloc[:,:3].as_matrix().astype(int)
y=data.iloc[:,3].as_matrix().astype(int)
from keras.models import Sequential
from keras.layers.core import Dense,Activation
model=Sequential()#建e立模型
model.add(Dense(input_dim=3,output_dim = 10))
model.add(Activation('relu'))#用relu函数做为隐含层激活函数,
model.add(Dense(input_dim=10,output_dim = 1))
model.add(Activation('sigmoid'))#由于是0-1输出，用sigmoid函数做为输出层激活函数
model.compile(loss='binary_crossentropy',optimizer='adam')
#编译模型，由于是二元分类，所以用的是bianry模式,求解方法我们指定为adam
model.fit(x,y,nb_epoch=1000,batch_size=10)#nb_epoch: 迭代次数
yp=model.predict_classes(x).reshape(len(y))#分类预测

from cm_plot import *
cm_plot(y,yp).show()