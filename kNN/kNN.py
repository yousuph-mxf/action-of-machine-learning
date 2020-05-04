import numpy as np
import operator
parameters:

    return:
        group
        labels

def createDataset():
    group = np.array([1,101],[5,89],[108,5],[115,8])
    #四组二维特征
    labels =['爱情片‘，’爱情片‘,'动作片','动作片']
    retuen group,lables
   
if _name_=='_main_':
   #创建数据流
   group,lables = createDataset()
   #打印数据流
   print(group)
   print(lablses)
