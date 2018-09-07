# -*- coding: utf-8 -*-
"""
@time:2018/7/15 15:59

@author: BX
"""
import os
print(os.getcwd())#获得当前的工作路径
#F:\PyCharm 2018.1.2\Mypython\untitled\analyse_data
os.chdir(r"F:\PyCharm 2018.1.2\Mypython\untitled\analyse_data")#改变当前工作路径
print(os.getcwd())#返回上级目录
os.chdir("..")#返回上级目录
os.makedirs("gouguoqi/gouguoqi1")#建立递归目录
os.chdir("gouguoqi/gouguoqi1")
os.mkdir("gouguoqi")#只能建一层
os.chdir("gouguoqi")

print(os.listdir(r"F:\PyCharm 2018.1.2\
Mypython\untitled\analyse_data"))#列出所有这个目录里面的文件
os.remove(r"F:\PyCharm 2018.1.2\Mypython\untitled\music\test.py")#删除指定文件
os.rename("plot_test","gouguoqinew")#修改文件夹名字
print(os.stat("gouguoqinew/testnew"))#查看文件的状态
print(os.sep)#当前路径系统的分隔符
print(os.linesep)#当前系统的行终止符
print(os.path.split('') )#  1个是目录路径 1个是文件名
os.path.dirname('')#拿路径分割的第一部分
os.path.basename ('')#拿路径分割第二部分
os.path.exists('')#判断路径是否存在
os.path.isabs('')#判断是否是绝对路径
os.path.isfile('')#判断文件是否存在
a="D:\pyproject"
b="day21模块\gouguoqinew"
print(os.path.join(a,b))#路径拼接
os.path.getmtime('')#文件最后修改的时间
