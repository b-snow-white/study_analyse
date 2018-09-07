# -*- coding: utf-8 -*-
"""
@time:2018/7/21 19:20

@author: BX
"""

from sklearn.metrics import confusion_matrix  # 导入混淆矩阵函数
import matplotlib.pyplot as plt  # 导入作图库
def cm_plot(y, yp,title):

    cm = confusion_matrix(y, yp)  # 混淆矩阵
    #print(cm)
    print('此模型在测试据集中的准确率为：',(cm[0][0]+cm[1][1])/len(y))
    #print()
    plt.matshow(cm, cmap=plt.cm.Greens)  # 画混淆矩阵图，配色风格使用cm.Greens，更多风格请参考官网。
    plt.colorbar()  # 颜色标签

    for x in range(len(cm)):  # 数据标签
        for y in range(len(cm)):
            plt.annotate(cm[x, y], xy=(x, y), horizontalalignment='center', verticalalignment='center')

    plt.ylabel('True label')  # 坐标轴标签
    plt.xlabel('Predicted label')  # 坐标轴标签
    plt.title(title)
    return plt