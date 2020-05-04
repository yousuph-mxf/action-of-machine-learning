import numpy as np
import operator

parameters:


return:
    group -数据流
    labels -分类标签

Modify:
    2017-07-13

"""
def createDataset():
    #四组二维特征
    labels = ['爱情片’，'爱情片',动作片','动作片']
    group = np.array([[1,101],[5,89],[108,5],[115,8]])
    return group,labels

parameters:
    inX  -用于分类的数据
    dataset -用于训练的数据
    labes -分类标签
    k -knn算法参数，选择距离的K个点
returns:
    sortedclasscount[0][0] -分类结果

Modify:
    2017-07-13
"""
def classsify0(inX,dataSet,labels,k):
    dataSetSize = dataSet.shap[0]
    #在列向量方向上重复inX共1次，行向量方向上重复inX共datasetsize次
    diffMat = np.tile(inX,(dataSetSieze,1))
    aqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances=sqDistances**0.5
    sorttedDistIndices = distances.argsort()
    classcount ={}
    for i in range(k):
        voteIlabel = labels[sorttedDistIndices[i]]
        classcount[voteIlabel] =classcount.get(voteIlabel,0) +1
        sortedClasscount =sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
        return sortedClassCount[0][0]


if __name__=='__main__':
    group,lables =createDataSet()
    test=[101,20]
    test_class = classify0(test,group,lables,3)
    #分类结果
    prin(test_class)
