# -*- coding: utf-8 -*-
"""
@time:2018/8/3 17:55

@author: BX
"""
import numpy as np
array=np.array([[1,2,3],[4,5,6]],dtype=int)#将数组变成矩阵
print(array.ndim,array.shape,array.size)#几维，形状，大小
a=np.zeros((4,3))#生成全为0的矩阵
b=np.ones((2,3))#生成全为1的
c=np.arange(10,20,2)
d=np.arange(12).reshape(3,4)#生成3行4列的数列
e=np.linspace(1,10,6).reshape(2,3)#生成线段

#计算
import numpy as np
a1=np.array([10,20,30,40])
b1=np.arange(4)
print(a1-b1,a1**2,10*np.sin(a1),np.cos(a1),np.tan(a1))#减法和平方,sin 的10倍,tan,cos
print(b1<3,b1==3)#元素小于3
#矩阵乘法
c1=np.array([[1,1],[0,1]])
d1=np.arange(4).reshape(2,2)
print(c1*d1)#逐个相乘
print(np.dot(c1,d1),c1.dot(d1))#矩阵相乘
e1=np.random.random((2,4))#生成0-1的2行4列的矩阵
print(np.sum(e1,axis=1),np.min(e1),np.max(e1))#按行或者列求值，1表示行，0表示列
A=np.arange(2,14).reshape(3,4)
print(np.argmin(A),np.argmax(A))#最小值的索引,最大值的索引
print(np.mean(A,axis=1),np.average(A),A.mean())#平均值,并且可以设置成行或者列
print(np.median(A))#中位数
print(np.cumsum(A),np.diff(A))#累加,累差
print(np.nonzero(A))#输出非零的索引
print(np.sort(A))#逐行排序
print(np.transpose(A),A.T.dot(A))#转置
print(np.clip(A,5,10))#截取中间的数，小于5的变成5，大于10的变成10

#索引,和列表一样
B=np.arange(3,15).reshape((3,4))
print(B[2][1],B[2,1],B[2,:])#索引出值,第二行的所有数
for row in B:#迭代行
    print(row)
for columns in B.T:#列的迭代
    print(columns)
for item in B.flat:#flat变成迭代器，逐个遍历
    print(item)

#合并
A=np.array([1,1,1])[:,np.newaxis]
B=np.array([2,2,2])[:,np.newaxis]
print(np.concatenate((A,B),axis=0))#合并可以按
print(np.vstack((A,B)),np.hstack((A,B)),A[np.newaxis,:])#上下合并,左右合并
print(A[np.newaxis,:],A[:,np.newaxis])#序列变成向

#分割
A=np.arange(12).reshape((3,4))
print(np.split(A,2,axis=1),np.array_split(A,3,axis=1),np.vsplit(A,3),np.hsplit(A,2))#纵向分割


#复制
a=np.arange(4)
b=a.copy()#b的值变，a 不变
a=b#a,b关联
a[0]=0.3
a.copy()
print(b is a)#True or False


