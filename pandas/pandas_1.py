import pandas
food_info = read_csv("food_info.csv")
print(type(food_info))
print(food_info.dtypes)
food_info.head()
#显示前五行
food_info.tail()
#显示后几行
print(food_info.shape)
print(food_info.loc[0])
#取出一个数据
food_info.loc[3：6]
#可以利用切片
ndb_col= food_info["NDB_NO"]
print(ndb_col)
#索引 列名

 






