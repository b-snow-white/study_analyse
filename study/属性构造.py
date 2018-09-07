# -*- coding: utf-8 -*-
"""
@time:2018/7/16 19:52

@author: BX
"""
#线损率属性构造
#参数初始化
import pandas as pd
inputfile=r'H:\data_test\chapter4\demo\data\electricity_data.xls'
outputfile=r'H:\data_test\chapter4\demo\tmp\electricity_data.xls'

data=pd.read_excel(inputfile)#读入数据
data['线损率']=(data['供入电量']-data['供出电量'])/data['供入电量']
data.to_excel(outputfile)
