#建立数据集
import numpy as np
import pandas as pd
from math import log
def cream_date_set():
    row_data={'no surfacing':[1,1,1,0,0],
             'flippers':[1,1,0,1,1],
             'fish':['yes','yes','no','no','no']}
    dateSet =pd.DataFrame(row_data)
    return  dateSet
"""
函数名称：cal_ent
函数功能：计算香农熵
"""
def cal_ent(dataSet):
    n=dataSet.shape[0]
    iset=dataSet.iloc[:,-1].value_counts()
    p=iset/n # 每类标签所占比
    ent=(-p*np.log2(p)).sum()
    return ent



date_set=cream_date_set()
print(date_set)#数据集
n=cal_ent(date_set)

""""
功能： 选择最优的列切"""
def bestsplit(dataSet):
    baseEnt=cal_ent(dataSet)
    bestGain=0
    axis=1
    for i in range(dataSet.shape[1]-1):
        levels=dataSet.iloc[:,i].value_counts().index
        ents=0
        for j in levels:
            childSet=dataSet[dataSet.iloc[:,i]==j]
            ent =cal_ent(childSet)
            ents+=(childSet.shape[0]/dataSet.shape[0])*ent
            infoGain = baseEnt-ents
            if(infoGain>bestGain):
                bestGain=infoGain
                axis=i
    return axis


"""
函数功能：按照给定的列划分数据集
参数说明：dateset 原始数据集
          axis:指定列索引
          value ;指定的属性值

  return 按照指定列索引和属性切分后的数据集"""

def mysplit(dataSet,axis,value):
    col=dataSet.colums[axis]
    redataSet=dataSet.loc[dataSet[col]==value,:].drop(col,axis=1)#利用bool型筛选
    return redataSet
