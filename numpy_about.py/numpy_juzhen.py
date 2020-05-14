import numpy as np
a = np.floor(10*np.random.random((3,4))
#floor 向下取整
print(a.ravel())
#将矩阵转化成数组 拉平
print(a.shape(6,2))
#改变行列
print(a.T)
#j矩阵转置
b = np.floor(10*np.random.random((2,2)))
c = np.floor(20*np.random.random((2,2)))
print(np.hstanck(b,c))
#拼接两个矩阵  横着拼  vstanck 竖着拼
d=np.hstanck(b,c)
print(np.vsplit(d,2)

#f分离 切割、
a_1 = np.arange(12)
a_2 =a_1
print(a_1 is a_2)
#返回bool型数据 true
a_2.shape =3,4
print(a_1.shape)
print(id(a_1))
print(id(a_2))
#这两个变量一样的 改变a_1 a_2也会改变的
a_3= a_1.view()
#a_1 与a_3公用一套值 但id不同的
a_4=a_1.copy()
#关于复制over

data = np.sin(np.arange(20).reshape(5,4)

ind = np.argmax(axis=0)
print(ind)
data_max= data[ind,range(data,shape[1]]
print(data_max)
#遍历找最大值
a_5=np,arange(0,40,10)
print(a_5)
b_5=np.tile(a,(3,5))
#把a以矩阵扩展
a_6= np.array([3,2,5],[8,6,10])
b_6=np.sort(a,axis=1)
a_61=a_6.ravel()
b_61=np.sort(a_61)
#f分别对矩阵 数组 排序
print(-------------)
a_7= np.array([4,7,3,2])
j=a.np.argsort(a)
#对从小到大的索引
print(a[j])
#就自然排好序了

