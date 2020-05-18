
import pandas
food_info = pandas.read_csv("food_info.csv")
col_names = food_info.columus.tolist()
print(col_names)
print(food_info.head())
##实现功能 查找列名中有特殊字符段的列名
gram_columns =[]

#遍历
for i in col_names:
    if c.endswith("(g)"):
        gram_columns.append(c)
gram_df = food_info[gram_columns]
print(gram_df.head())
print(--------------------------)
#列表简单计算
water_energy = food_info["water_(g)]*food_info["Energ_kcal"]
#简单计算 + - /一样的格式

