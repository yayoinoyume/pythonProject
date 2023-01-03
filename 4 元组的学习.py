#列表适合用于存储在程序允许期间可能变化的数据集，列表是可以修改的，但有时候需要创建一些不可修改的
#元素，这个时候就需要用到元组。

#元组的许多语法都与列表相同
#元组相关的大部分语法都只是把列表语法里的[]变成了()、

#元组的创建
dimensions = (1,2,3,4,5,6,7,8,)
print(dimensions)

#遍历元组，利用for循环
for dimension in dimensions:
    print(dimension)

#“修改”元组的变量 实际上只能通过定义一个新元组来达到修改元组的目的
dimensions = (10,200)
for dimension in dimensions:
    print(dimension)
dimensions = (30,300)
for dimension in dimensions:
    print(dimensions)




















