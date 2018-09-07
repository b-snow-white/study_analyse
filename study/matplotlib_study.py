 # -*- coding: utf-8 -*-
"""
@time:2018/8/5 12:01

@author: BX
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
'线性方程'
#figure,show,plot
# x=np.linspace(-1,1,50)
# y1=2*x+1
# y2=x**2+1
# plt.figure()
# plt.plot(x,y1,'g')#g,r,y,b
# plt.figure(num=3,figsize=(8,6))
# '坐标轴设置'
# plt.xlim((-1,2))#坐标轴范围
# plt.ylim((-2,3))
# plt.xlabel('I am y')#坐标轴标签
# plt.ylabel('I am x')
# new_ticks=np.linspace(-1,2,5)#坐标轴数据a
# plt.xticks(new_ticks)#替换xticks
# plt.yticks([-2,-1.8,-1,1.22,3],
#            [r'$really\ good$',r'$bad\ \alpha$',r'$normal$',r'$good$',r'$really\ good$'])#$变成数学形式的字体
# #gca=get current axis
# ax=plt.gca()#拿出轴
# ax.spines['right'].set_color('none')#轴的边框
# ax.spines['top'].set_color('none')
# ax.xaxis.set_ticks_position('bottom')#坐标轴用哪一个轴代替，相当于产生了x轴
# ax.yaxis.set_ticks_position('left')#相当于产生了y轴
# #设置坐标轴位置
# ax.spines['bottom'].set_position(('data',0))#设置横轴在y轴数据的-1，axes,定位到百分之多少的位置
# ax.spines['left'].set_position(('data',0))
#
# '图例设置'
# l1,=plt.plot(x,y2,'r',label='up')
# l2,=plt.plot(x,y1,'b--',linewidth=2,label='down')
# plt.legend(handles=[l1,l2,],labels=['a','b'],loc='best')#loc为best表示把标签放到最好的位置
#
# '添加注释'
# x=np.linspace(-3,3,50)
# y=2*x+1
# plt.figure(num=4,figsize=(8,5))
# plt.plot(x,y)
# ax=plt.gca()#拿出轴
# ax.spines['right'].set_color('none')#轴的边框
# ax.spines['top'].set_color('none')
# ax.xaxis.set_ticks_position('bottom')#坐标轴用哪一个轴代替，相当于产生了x轴
# ax.yaxis.set_ticks_position('left')#相当于产生了y轴
# #设置坐标轴位置
# ax.spines['bottom'].set_position(('data',0))#设置横轴在y轴数据的-1，axes,定位到百分之多少的位置
# ax.spines['left'].set_position(('data',0))
# x0=1
# y0=2*x0+1
# plt.scatter(x0,y0,s=50,color='b')
# plt.plot([x0,x0],[y0,0],'k--',lw=2.5)
# #method 1
# plt.annotate(r'$2x+1=%s$'%y0,xy=(x0,y0),xycoords='data',xytext=(+30,-30),textcoords='offset points',fontsize=16,arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=.2'))
# #method 2
# plt.text(-3,3,r'$This\ is\ some\ text.\ \mu \sigma_i \alpha_t$',fontdict={'size':16,'color':'r'})
#
#
# '线遮住的部分设置透明度'
# x=np.linspace(-3,3,50)
# y=0.1*x
# plt.figure()
# plt.plot(x,y,linewidth=10,zorder=1)#需要在for里面设置zoeder比原来的大
# plt.ylim(-2,2)
# ax=plt.gca()#拿出轴
# ax.spines['right'].set_color('none')#轴的边框
# ax.spines['top'].set_color('none')
# ax.xaxis.set_ticks_position('bottom')#坐标轴用哪一个轴代替，相当于产生了x轴
# ax.yaxis.set_ticks_position('left')#相当于产生了y轴
# #设置坐标轴位置
# ax.spines['bottom'].set_position(('data',0))#设置横轴在y轴数据的-1，axes,定位到百分之多少的位置
# ax.spines['left'].set_position(('data',0))
# for label in ax.get_xticklabels() + ax.get_yticklabels():
#     label.set_zorder(2)
#     label.set_fontsize(12)
#     label.set_bbox(dict(facecolor='white',edgecolor='None',alpha=0.7))


'散点图'
# n=1024
# x=np.random.normal(0,1,n)
# y=np.random.normal(0,1,n)
# T=np.arctan2(y,x)#产生随机的颜色
# plt.scatter(x,y,s=75,c=T,alpha=0.5)
# plt.xlim((-1.5,1.5))
# plt.ylim((-1.5,1.5))
# plt.xticks(())#x轴坐标没有标签
# plt.yticks(())
# plt.show()

'柱状图'
# n=12
# x=np.arange(n)
# y1=(1-x/float(n))*np.random.uniform(0.5,1.0,n)
# y2=(1-x/float(n))*np.random.uniform(0.5,1.0,n)
# plt.bar(x,+y1,facecolor='#ADD8E6',edgecolor='white')
# plt.bar(x,-y2,facecolor='#ff9999',edgecolor='white')
# for x,y in zip(x,y1):
#     plt.text(x,y+0.05,'%.2f'%y,ha='center',va='bottom')
# x=np.arange(n)
# for x,y in zip(x,y2):
#     plt.text(x,-y-0.05,'-%.2f'%y,ha='center',va='top')
# plt.xlim(-5,n)
# plt.xticks(())
# plt.ylim(-1.25,1.25)
# plt.yticks(())


'等高线图'
def f(x,y):
    return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)
n=250
x=np.linspace(-3,3,n)
y=np.linspace(-3,3,n)
X,Y=np.meshgrid(x,y)#x,y绑定网格的输入值
plt.contourf(X,Y,f(X,Y),4,alpha=0.75,cmap='hot')#定义高线和颜色和8表示化成10部分
C=plt.contour(X,Y,f(X,Y),4,colors='black',linewidth=.5)#画出等高线
plt.clabel(C,inline=True,fontsize=10)#每个等高线有标签

'图形'
# a=np.array([]).reshape(())
# plt.imshow(a,interpolation='nearest',cmap='bone',origin='lower')#origin还有uuper，interpolation有很多形式
# plt.colorbar(shrink=0.9)#添加右边条形说明
# plt.xticks(())
# plt.yticks(())
# plt.show()

'3D画图'
from mpl_toolkits.mplot3d import Axes3D
fig=plt.figure()#画框
ax=Axes3D(fig)#坐标轴
X=np.arange(-4,4,0.25)
Y=np.arange(-4,4,0.25)
X,Y=np.meshgrid(X,Y)#底面
R=np.sqrt(X**2+Y**2)
Z=np.sin(R)

ax.plot_surface(X,Y,Z,rstride=2,cstride=2,cmap=plt.get_cmap('rainbow'))
ax.contourf(X,Y,Z,zdir='z',offset=-2,cmap='rainbow')#等高线的位置
ax.set_zlim(-2,2)


'创建小图'
plt.figure()
plt.subplot(2,1,1)
plt.plot([0,1],[0,1])
plt.subplot(2,3,4)
plt.plot([0,1],[0,2])
plt.subplot(2,3,5)
plt.plot([0,1],[0,3])
plt.subplot(2,3,6)
plt.plot([0,1],[0,4])

'subplot分格显示'
#plt.subplot2grid()
# plt.figure()
# ax1=plt.subplot2grid((3,3),(0,0),colspan=3,rowspan=1)
# ax1.plot([1,2],[1,2])
# ax1.set_xlabel('x')
# ax2=plt.subplot2grid((3,3),(1,0),colspan=2)
# ax3=plt.subplot2grid((3,3),(1,2),rowspan=2)
# ax4=plt.subplot2grid((3,3),(2,0))
# ax5=plt.subplot2grid((3,3),(2,1))

#plt.gridspec
# import matplotlib.gridspec as gridspec
# plt.figure()
# gs=gridspec.GridSpec(3,3)
# ax1=plt.subplot(gs[0,:])
# ax2=plt.subplot(gs[1,:2])
# ax3=plt.subplot(gs[1:,2])
# ax4=plt.subplot(gs[-1,0])
# ax5=plt.subplot(gs[-1,-2])


#plt.subplots()
f,((ax11,ax12),(ax21,ax22))=plt.subplots(2,2,sharex=True,sharey=True)
ax11.scatter([1,2],[1,2])

'图中图'
fig=plt.figure()
x=[1,2,3,4,5,6,7]
y=[1,3,4,2,5,8,6]
left,bottom,width,height=0.1,0.1,0.8,0.8
ax1=fig.add_axes([left,bottom,width,height])
ax1.plot(x,y,'r')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_title('title')
left,bottom,width,height=0.2,0.6,0.25,0.25
ax2=fig.add_axes([left,bottom,width,height])
ax2.plot(y,x,'b')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_title('title inside 1')

plt.axes([0.6,0.2,0.25,0.25])
plt.plot(y[::-1],x,'g')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('title inside 1')


'次坐标'
x=np.arange(0,10,0.1)
y1=0.05*x**2
y2=-1*y1
fig,ax1=plt.subplots()
ax2=ax1.twinx()
ax1.plot(x,y1,'g--')
ax2.plot(x,y2,'b-')
ax1.set_xlabel('X data')
ax1.set_ylabel('Y1',color='g')
ax2.set_ylabel('Y2',color='b')
ax1.set_title('test')

'动图，必须在ide中编辑'
from matplotlib import animation
fig1,ax=plt.subplots()
x=np.arange(0,2*np.pi,0.01)
line,=ax.plot(x,np.sin(x))
def animation1(i):
    line.set_ydata(np.sin(x+i/10))#更新
    return line,
def init():
    line.set_ydata(np.sin(x))
    return line,
#随着时间变动的function,闪过100个时间点，隔20毫秒更新一次
ani=animation.FuncAnimation(fig=fig1,func=animation1,frames=100,init_func=init,interval=20,blit=False)#interval表示每隔20秒更新一次

plt.show()