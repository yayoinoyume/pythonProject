#遍历整个列表 for item in list_of_items
words = ['a','b','c','d','e','f','g','h','i']
for word in words:
    print(word)
#使用for时，要注意缩进，缩进后的代码都将参与for循环，而不缩进的代码只会执行一次
#使用for时，要注意句尾的:  遗漏会导致语法错误

#创建数值列表 range语句
value = range(1,10)
print(value)
#输出结果是1到9，range有头没有尾
#在使用range时，默认步长为1，但也可以随意指定步长
value2 = range(1,10,2)

#range生成的是一串数字，如果要将这些数字存入列表，需要结合list语句,
#list()是将括号内的东西化作一个列表
print(list(range(2,10,2)))
#输出结果是[2,4,6,8,10]

#如果想要中途将range产生的值加入列表，可以先创建一个列表，然后利用append将value依次添加进列表
#创建一个空列表
numbers = []
#因为append每次只能添加一个元素，所以想要用一个append添加多个元素，需要配合for循环
for value in range(1,21):
    number = value
    numbers.append(number)

print(numbers)

#更简洁的等效代码是,就不需要再借助临时变量number了
numbers = []
for value in range(1,21):
    numbers.append(value)

print(numbers)


#对列表执行简单的统计计算
digits = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
#求最小值
print(min(digits))
#求最大值
print(max(digits))
#求和
print(sum(digits))

##列表解析
#列表解析将for循环和创建新元素的代码合并成一行，并且自动附加新元素
squares = [value for value in range(1,21)]
print(squares)

#要使用列表解析，首先创建一个空列表，之后，在[]内添加for循环 for 表达式 in 范围
#在列表解析中，for语句末尾没有冒号


#练习1 用 for 循环输出数字1-20
list1 =[value for value in range(1,21)]
print(list1)

#练习2
list2 = [value for value in range(1,1000000001)]
for value in list2:
    print(value)
print(sum(list2))

#通过range函数创建一个值包含能被3整除的数的列表
#能被3整除的数字的特点是这个数字是由3开始经过n个3步长得到的
list3 = [value for value in range(3,99,3)]
for value in list3:
    print(value)

#创建一个列表，内容是0-20内所有整数的三次方，并输出
list4 = [value**3 for value in range(3,21)]
for value in list4:
    print(value)

#提取列表中的元素（制作切片）
list5 = ['a','b','c','d','e','f','g','h','i','j']
print(list5[0:4])
#输出结果是abcd，含头不含尾，从零开始记数

#如果元素很多，而你只想输出最后三名，就用[-3:]就好了，当不指名坐标的时候，默认从头或到尾


#利用切片的原理去复制列表
list5 = ['a','b','c','d','e','f','g','h','i','j']
list6 = list5[:]
#[:]这个地方相当于从头复制到尾，这种复制所产生的列表与原列表无关系，只是单纯有元素的重合

#另一种错误的复制列表的方式是直接令两个列表相等
list5 = list6
#这个时候，不论是list5 还是list6都指向了同一个列表，他们相互关联，当修改列表时，不论是list5还是
#list6都会同步修改









