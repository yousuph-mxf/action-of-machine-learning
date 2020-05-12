import numpy as np
print(np.arange(15))
#[0 1  2 3 4 5 6 7 8 9 10 11 12 13 14]
a = np.arange(15).reshape(3,5)
#转换成矩阵的形式
a_1=a.nidm()
#求出几行几列哈
a_2=a.size()
#求出元素个数
a_3=np.zeros((3,4))
#初始化矩阵 三行四列 值为0
a_4=np.ones((3,4))
#
a_5=np.arange(10,30,5)
#printf [10,15,20,25]
a_6=np.random.ramdom((2,3))
#产生一个随机生成的数组
form numpy import pi
a_7=np.linspace(0,2*pi,100)
#在0到2*pi之间 生成100个数
b= np.arange(4)
c= np.array([20,30,40,50])
d=c-b
#对应项之间，相减
d_1=b**2
#对应项之间 平方
print(c<20)
#对应项之间 返回bool型数组
#矩阵算法

A=np.array([1,1],
           [0,1])
B=np.array([2,0],
           [3,4])
print(A*B)#对应位置相乘
print(A.dot(B))
