import pandas
food_info = pandas.read_csv("food_info.csv")
#排序相关操作哈
food_info.sort_values("Sodium_(mg)",inplace=True)
print(food_info["Sodium_(mg)"])
##sort)values 默认升序
food_info.sort_values("Sodium_(mg)",inplase=True,ascending=False)
print(food_info)

