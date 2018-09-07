# -*- coding: utf-8 -*-
"""
@time:2018/7/15 21:43

@author: BX
"""
import pandas as pd
import numpy as np
datafile=r'H:\data_test\chapter4\demo\data\normalization_data.xls'
data=pd.read_excel(datafile,header=None)
(data-data.min())/(data.max()-data.min())#最小-最大规范化
(data-data.mean())/data.std()#零-均值规范化
data/10**np.ceil(np.log10(data.abs()).max())#小数定标规范化（将数定位到【-1,1】）

