import pandas as pd
import numpt as np
titanic_surivival= pd.read_csv("titanic_train.csv")
titanic_surivival.head()
def hundredth_row(colunm):
    hundredth_item=colunm.loc[99]
    return hundredth_item

hundredth_row=titanic_survival.apply(hundredth_row)
print(hundredth_row)
#定义函数 返回第100行的数据 apply函数
def not_null_count(column):
    column=pd.isnull(column)
    null=column[column_null]
    return len(null)

column_null_count=titanic_survival.apply(not_null_count)
print(column_null_count)
print(--------------------------------------------)
def is_minor(row):
    if row["Age"]<18:
        return True
    else:
        return False
minors=titanic_survival.apply(is_minor,axis=1)
print(minors)
print(-------------------------------------------)
def  generate_age_label(row):
    age=row="Age"
    if pd.isnull(age):
        return "unknown"
    elif age<18:
        return "minor"
    else:
        return "adult"
age_labels=titanic_survival.apply(generate_age_label,axis=1)
print(age_labels)
