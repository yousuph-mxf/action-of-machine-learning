import  pandas as pd
import matplotlib as mat
import matplotlib.pyplot as plt

"""
函数功能：用knn算法实现约会配对
"""
datingtest=pd.read_table('datingTestSet.txt',header=None)
colors=[]
for i in range(datingtest.shape[0]):
    m=datingtest.iloc[i,-1]
    if m=='didntLike':
        colors.append('black')
    if m=='smallDoses':
        colors.append('orange')
    if m=='largeDoses':
        colors.append('red')

plt.rcParams['font.sans-serif']=['Simhei']#图中字体设置为黑体
pl=plt.figure(figsize=(12,8))
fig1=pl.add_subplot(221)
plt.scatter(datingtest.iloc[:,1],datingtest.iloc[:,2],marker='.',c=colors)
plt.xlabel('玩游戏所占时间比')
plt.ylabel('xixix')


# 函数说明：对于每年飞行时间对结果影响太大了，数据归一化
def minmax(dataSet):
    mind=dataSet.min()
    maxd=dataSet.max()
    norSet=(dataSet-mind)/(maxd-mind)
    return norSet
datingT=pd.concat([minmax(datingtest.iloc[:, :3]),datingtest.iloc[:,3]],axis=1)
print(datingT.head())

def randsplit(dataSet,rate=0.9):
    n=dataSet.shape(0)
    m=int(n*rate)
    train=dataSet.iloc[:m,:]
    test=dataSet.iloc[m:,:]
    test.index=range(test.shape[0])
    return train,test
train,test=randsplit(datingT)
print(train)
