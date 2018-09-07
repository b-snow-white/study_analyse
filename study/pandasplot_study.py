# -*- coding: utf-8 -*-
"""
@time:2018/8/5 11:48

@author: BX
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
'折线'
#series
data=pd.Series(np.random.randn(1000),index=np.arange(1000))
data=data.cumsum()
data.plot()
plt.show()
#DataFrame
data=pd.DataFrame(np.random.randn(1000,4),index=np.arange(1000),columns=['A','B','C','D'])
data=data.cumsum()
data.plot()
plt.show()
'散点'
#scatter
ax=data.plot.scatter(x='A',y='B',color='DarkBlue',label='Class1')
data.plot.scatter(x='A',y='C',color='DarkGreen',label='Class2',ax=ax)
plt.show()
'plot method'
#bar,hist,box,kde,area,scatter,hexbin,pie

