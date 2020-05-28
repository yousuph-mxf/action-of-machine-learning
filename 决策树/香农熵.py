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
函数名称：calent
函数功能：计算香农熵
"""
def cal_ent(dataSet):
    n=dataSet.shape[0]
    iset=dataSet.iloc[:,-1].value_counts()
    p=iset/n# 每类标签所占比
    ent=(-p*np.log2(p).sum())
    return ent



date_set=cream_date_set()
print(date_set)#数据集
print(cal_ent(date_set))
