#列表由一系列按照特定顺序排列的元素组成，各个元素之间没有任何关系
#列表用[]来表示,其中的元素用''来包含，元素之间用,来分隔,例如
bicycles = ['TREK','cannondale','forever','Java']
print(bicycles)

#访问列表中的元素
#列表会对其中的元素从0开始编号，通过编号，我们能对列表中的元素进行索引
#输出的结果不会包含''和,  而是直接输出字符
bicycles = ['TREK','cannondale','forever','Java']
print(bicycles[1])
print(bicycles[2])
#疑问，怎么一次索引多个列表中不连续的元素？？？？？？？？？？？？？？？？？？？？？

#配合第一章中所学的对字符串的处理
print(bicycles[2].title())

#有时候，列表包含了非常多的元素，以至于我们无法清楚最后一个元素是正数第几号，但我们可以通过倒数来索引
print(bicycles[-1])
#这个的输出结果就是最后一号元素Java


#简单练习 I want to own a ()
list = ['Car','Xiaomi 13 pro 12+512','Xiaomi watch S2 46','cash','strong PC']
print("I want to own a" + list[1])


#在列表中修改元素
#思路：要修改列表元素，可以指定列表名和要修改的列表元素的索引，再指定该元素的新值。
list1 = [1,2,3,4,5]
print(list1)
list1[0] = 100
print(list1)

#在列表中添加元素（插入元素）
#在列表中添加元素，默认会添加到列表末尾，这也是最简单的添加方式
#利用append()的方法来添加元素，添加的元素位置只能是末尾
list1 = [1,2,3,4,5]
print(list1)
list1.append(100)
print(list1)

#在列表中的任何位置插入元素，需要用到insert()insert()的用法是insert(坐标,添加的元素)
list1 = [1,2,3,4,5]
print(list1)
list1.insert(0,100)
print(list1)

#从列表中删除元素
#从列表中删除元素，有两种形式，一种是将此元素完全抹去，另一种是将此元素从原列表中提出
#两种形式对应的删除指令分别为del或remove和pop(元素位置)

#del的用法,del需要知道元素在列表中的位置，如果列表元素太多，我们无法确定指定元素的位置
#我们也可以根据元素来删除，也就是remove。
list1 = [1,2,3,4,5,6,7,8,'a','b','c','d','e','f']
print(list1)
del list1[2]
print(list1)
list1.remove('a')
print(list1)

#也可以按照类似pop的方法使用，但是本质上还是强行抹除，不存在剪切的行为
list1 = [1,2,3,4,5,6,7,8,'a','b','c','d','e','f']
useless = 'a'
print(list1)
list1.remove(useless)
print(list1)

#pop()的用法,pop可以做到在提取出元素后重新存取到新的列表中，类似于剪切
#当然，如果不粘贴，也是完全抹除
list1 = [1,2,3,4,5,6,7,8,'a','b','c','d','e','f']
print(list1)
list1_popped = list1.pop(2)
print(list1)
print(list1_popped)

#练习
#1.创建一个列表，包含三个及以上你想邀请的人，并使用此列表打印邀请信息
list = ['Peter', 'Bob', 'John', 'Jack', 'Maria', 'Zaion', 'Pomu']
print("Dear " + list[0] + ",I would like to invite you to have dinner with me in my house.")

#修改此名单
list[0] = "Amamiya"
print(list)

#添加人员
list.append("Finana")
print(list)

###############################################################

#使用sort对列表进行永久性排序
list = ['b','a','d','c','f','e']
print(list)
list.sort()
print(list)
#这样操作之后，列表中的所有元素都会按照字母顺序进行排列
#sort()方法用原地算法对数组的元素进行排序，并返回数组。
#默认排序顺序是在将元素转换为字符串，然后比较它们的UTF-16代码单元值序列时构建的(看不懂)

#也可以用sorted对列表进行临时排序
list = ['b','a','d','c','f','e']
#展示初始列表
print(list)
#对列表进行临时排序并输出结果
print(sorted(list))
#再次打印原列表，检查顺序是否被打乱
print(list)

#同样的，如果想要倒序着打印列表，可以使用reverse()，用法和sort相同
list = ['b','a','d','c','f','e']
print(list)
list.reverse()
print(list)
#可以看到上述指令的输出结果只是直接把这个列表倒着输出了一遍
#如果我们想要修改列表的排序，让它按照字母顺序由大到小输出
#那么就可以结合一下sort和reverse
list = ['b','a','d','c','f','e']
print(list)
list.sort(reverse=True)
print(list)

#获取列表的长度
#列表中的长度，即列表中包含的元素个数，记数从1开始

#练习，想出至少5个我想去的地方，并将这些地方存储在一个列表中
place = ['d','f','b','s','h','n']
print(place)

#按照sorted的顺序打印这个列表
###错误代码(place.sort())
print(sorted(place))
#再次打印这个列表，验证顺序没有变
print(place)

#使用sorted按照倒序临时修改并打印列表
###错误代码print(place.sortted(reverse=True))
print(sorted(place,reverse=True))
#再次打印列表，验证顺序没变
print(place)

#使用reverse修改列表顺序，再打印此列表，证明顺序确实变了
place.reverse()
#再次使用reverse，使列表恢复
place.reverse()
















