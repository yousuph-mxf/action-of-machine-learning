import pandas as pd
import numpt as np
titanic_surivival= pd.read_csv("titanic_train.csv")
titanic_surivival.head()
age= titanic_survival["Age"]
age_is_null = pd.isnull(age)
#返回bool类型的数值
age_null_true=age[age_si_null]
#索引
age_null_count=len(age_null_true)
#计算null的个数哈
print(-----------------------------------------)
mean_age = sum(titanic_surivival["Age"])/len(titanic_surivival["Age"])
print(mean_null)
#有空格的话 无法正常计算 返回null
good_ages =titanic_survival["Age"][age_is_true==False]
correct_mean_age= sum(good_ages)/len(good_ages)
print(correct_mean_age)
print(-------------------------------------------------)
#统计
passener_survival=titanic_survival.pivot_tabls(index="Pclass",values="Survived",aggfunc=np.mean)
print(passenger_survival)
port_stats=titanic_survival.pivot_table(index="Embarked",values=["Fare","SUrvived"].aggfunc=np.sum)
##计算embarked 与fare ,suvived之间的关系
new_titanic_survival=titanic_survival>sort_values("Age",ascending=False)
print(new_titanic_survival[0:10])
#这两个之间就是排列的区别，前者序号是列号，后者是从0开始
titanic_reindexed=new_titanic_survival.reser_index(drop=True)
print(titanic_reindexed)
