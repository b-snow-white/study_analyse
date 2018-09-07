# -*- coding: utf-8 -*-
"""
@time:2018/8/3 19:36

@author: BX
"""
import pandas as pd
import numpy as np
df=pd.Series(['an',1,np.nan])
dates=pd.date_range('20180804',periods=6)#产生时间序列
df1=pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])#产生datafame

'基础函数'
df1.shape()#产生几行几列
len(df1.index)#总共有多少行数据


's数据筛选'
#strait selection
print(df1['A'],df1.A)
print(df[0:3],df['20180805':'20180806'])
#selecion by label:loc
print(df.loc['20180806'],df.loc[:,['A','B']],df.loc['20180805',:])
#selection by position:iloc
print(df.iloc[3],df.iloc[3:5,1:3],df.iloc[[1,3,4],1:3])
#selection by mixed:ix
print(df.ix[:3,['A','B']])#既可以label又可以position
print(df[df.A>8])#boleaning indexing
print(df[df.A.isin([5,6])])#判断5,6是否在A列并输出数据

'数据修改'
#df.iloc['20180806','B']=222
df.loc['20180806','B']=2
df[df.A>4]=0
df.B[df.A>4]=0
df['F']=np.nan
df['E']=pd.Series([1,2,3,4,5,6],index=dates)
df.iloc[0,1]=np.nan

'空值判断'
df.isnull()#boleaning value
print(np.any(df1.isnull())==True)


'处理空值NaN=np.nan'
df1.dropna(axis=1,how='any')#how={all,any},any表示只要有一个空值，则删除
df1.fillna(value=0)
print(np.any(df.isnull())==True)#有没有丢失值,返回boolean

'导入或者导出'
pd.read_csv()
pd.to_pickle()

'数据合并:concat'
a=pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])
b=pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'])
c=pd.DataFrame(np.ones((3,4))*2,columns=['a','b','c','d'])
res=pd.concat([a,b,c],axis=0,ignore_index=True)#竖向合并,并且索引连续
a1=pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'],index=[1,2,3])
b1=pd.DataFrame(np.ones((3,4))*1,columns=['b','c','d','e'],index=[2,3,4])
res1=pd.concat([a1,b1],join='inner',ignore_index=True)#只把相同的合并
res2=pd.concat([a1,b1],axis=1,join_axes=[a1.index])#只考虑a1的index
a1.append([b1,a],ignore_index=True)#往竖向加数据
s1=pd.Series([1,2,3,4],index=['a','b','c','d'])
a2=pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])
res4=a2.append(s1,ignore_index=True)
'数据合并：merge'
left=pd.DataFrame({
    'Key':['K0','K1','K2','K3'],
    'A':['A0','A1','A2','A3'],
    'B':['B0','B1','B2','B3']
})
right=pd.DataFrame({
    'Key':['K0','K1','K2','K3'],
    'C':['C0','C1','C2', 'C3'],
    'D':['D0','D1','D2','D3']
})
pd.merge(left,right,on='Key')#基于key合并
left=pd.DataFrame({
    'Key1':['K0','K0','K1','K2'],
    'Key2':['K0','K1','K0','K1'],
    'A':['A0','A1','A2','A3'],
    'B':['B0','B1','B2','B3']
})
right=pd.DataFrame({
    'Key1':['K0','K1','K1','K2'],
    'Key2':['K0','K0','K0','K0'],
    'C':['C0','C1','C2', 'C3'],
    'D':['D0','D1','D2','D3']
})
on={'left','right','outer','inner'}#outer是自然合并,right基于右边连接
pd.merge(left,right,on=['Key1','Key2'],how='inner')#只把相同的合并
df1=pd.DataFrame({
    'col1':[0,1],'col_left':['a','b']
})
#显示merge
df2=pd.DataFrame({'col1':[1,2,2],'col_right':[2,2,2]})
pd.merge(df1,df2,on='col1',how='outer',indicator=True)#怎么样进行merge,想改名字就给indicator赋值
#基于index的合并
left=pd.DataFrame({'A':['A0','A1','A2'],'B':['B0','B1','B2'],'index':['K0','K1','K1']})
right=pd.DataFrame({'C':['C0','C2','C3'],'D':['D0','D2','D3'],'index':['K0','K2','K3']})
pd.merge(left,right,left_index=True,right_index=True,how='outer')

#解决重叠
boys=pd.DataFrame({'K':['K0','K1','K2'],'age':[1,2,3]})
girls=pd.DataFrame({'K':['K0','K0','K3'],'age':[4,5,6]})
pd.merge(boys,girls,on='K',suffixes=['_boys','_girls'],how='inner')
'join和merge很相似'


#