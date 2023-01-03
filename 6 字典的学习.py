#字典是一系列的键~值对，就如同现实中的字典一样，python中的字典也是通过键来查找存储在其中的值的
#字典的符号是{}
#指定键和值时，二者用:连接，创建一个字典的完整代码如下
alien_0 = {'a': 0, 'b': 1, 'c': 2, 'd': 3}

#字典的添加，添加键值对,添加语句中，使用[]
alien_1 = {'a': 0, 'b': 1, 'c': 2, 'd': 3}
print(alien_1)
alien_1['e'] = 4
alien_1['f'] = 5
print(alien_1)

#字典中值的修改
alien_2 = {'a': 0, 'b': 1, 'c': 2, 'd': 3}
print(alien_2)
alien_2['d'] = 4
print(alien_2)

#字典中键值对的删除
alien_3 = {'a': 0, 'b': 1, 'c': 2, 'd': 3}
print(alien_3)
del alien_3['a']
print(alien_3)
#这样的删除是键和值一起永久的删除，因为字典不允许值和键各自单独存在
#对于相似键值对构成的字典，要尽量避免在同一行排列

alien_3 = {
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3
}
#当字典比较复杂时，采取这样的格式会让字典变得清晰明确


#遍历字典  遍历所有键值对.items()
dict_1 = {
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 4,
    'f': 5,
    'g': 6
}
for key , value in dict_1.items():
    print("(" + key + "," + str(value) + ")")
print(dict_1.items())
#这里的dict1_items是由有序数对组成的列表



#遍历字典，遍历所有键
#在不需要知道字典的值得时候，方法.keys()很有用
dict_2 = {
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 4,
    'f': 5,
    'g': 6
}
for key in dict_1.keys():
    print(key)
#实际上，keys()的功能应该是，提取字典中的所有键并生成一个key列表
print(dict_1.keys())

#有顺序地遍历字典中的所有键，使用sorted(在列表简介一节中使用过，是暂时改变顺序的指令）
dict_3 = {
    'a': 0,
    'd': 1,
    'e': 2,
    'c': 3,
    'b': 4,
    'g': 5,
    'f': 6
}
for key in sorted(dict_3.keys()):
    print(key)
print(dict_3.keys())

#遍历字典中的所有值，使用values()，和遍历所有的键几乎相同
#需要注意的是，在字典中，键和值一一对应，和数学中的函数相同，键不会有重复，但值可能会有重复
#因此，遍历所有值的时候，我们可以利用集合的特性来去重
dict_4 = {
    'a': 0,
    'd': 0,
    'e': 3,
    'c': 3,
    'b': 4,
    'g': 5,
    'f': 6
}
#未去重的输出
for value in dict_4.values():
    print(value)
#去重的输出
for value in set(dict_4.values()):
    print(value)


#嵌套
#有时候，需要将一些字典存储在列表中，或者将列表作为值存储在字典中，这成为嵌套，你可以在列表中嵌套
#字典，在字典中嵌套列表甚至在字典中嵌套字典

#在列表中嵌套字典
#创建多个字典，并将其存储在列表中，利用列表的for循环，一次性输出多个字典内的信息
alien_0 = {'a': 0, 'b': 1, 'c': 2, 'd': 3}
alien_1 = {'a': 0, 'b': 1, 'c': 2, 'd': 3}
alien_2 = {'a': 0, 'b': 1, 'c': 2, 'd': 3}

aliens = [alien_1,alien_2,alien_0]
for alien in aliens:
    print(alien)

#快速创建多个字典并嵌套进列表中
#首先，创建一个用于存储的新列表
aliens = []
#利用循环，创建三十个外星人，并且对其编号
for alien_number in range(0,31):
    new_alien = {'a': 0, 'b': 1, 'c': 2, 'd': 3}
    aliens.append(new_alien)
#这样，一个包含三十个外星人信息的列表就创建好了，之后，需要清晰地把这个列表输出出来
for alien in aliens:
    print(alien)

#在字典中嵌套列表
#有时候，需要把列表嵌套在列表中
#应用的场景，大概就是需要使用一个键，一次输出“多个值”，这个时候，把值转化为列表
#例如，存储比萨的信息
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }

# 概述所点的比萨
print("You ordered a " + pizza['crust'] + "-crust pizza " +
    "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)

#每当需要在字典中将一个键关联到多个值时，都可以在字典中嵌套一个列表。
#又例如，一个人有多钟喜欢的语言
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }

for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())

#在字典中存储字典
#可在字典中嵌套字典，但这样做时，代码可能很快复杂起来。
#例如，如果有多个网站用户，每个都有独特的用户名，
#可在字典中将用户名作为键，然后将每位用户的信息存储在一个字典中，并将该字典作为与用户名相关联的值。
#在下面的程序中，对于每位用户，我们都存储了其三项信息：名、姓和居住地；
#为访问这些信息，我们遍历所有的用户名，并访问与每个用户名相关联的信息字典：
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },

    }

for username, user_info in users.items():
    print("\nUsername: " + username)

    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())

#列表和字典的嵌套层级不应太多。如果嵌套层级比前面的示例多得多，很可能有更简单的解决问题的方案。

#练习6-8 宠物：创建多个字典，对于每个字典，都使用一个宠物的名称来给它命名；
#在每个字典中，包含宠物的类型及其主人的名字。
#将这些字典存储在一个名为pets的列表中，再遍历该列表，并将宠物的所有信息都打印出来。

#首先，创建多个字典
cat = {'a': 0, 'b': 1, 'c': 2, 'd': 3}
dog = {'a': 0, 'b': 1, 'c': 2, 'd': 3}
fish = {'a': 4, 'b': 1, 'c': 2, 'd': 3}
bird = {'a': 5, 'b': 1, 'c':3}

#创建一个包含上述四个字典的列并输出
pets = [cat, dog, fish, bird]
for pet in pets:
    print(pet)


#个人感觉字典这一章学的知识很多，自己不擅长的往往是在与前面知识结合的部分
#可能是我还没有完全熟悉吧，虽然说这本入门书的基础知识部分算是学了一半了，但是还没来得及去巩固
#后续的实战应该是有必要认真学习的，课后的练习题，总觉得有些繁琐，但是可以看一下答案解析？
#因为今天去写的时候，发现自己写的代码真的连编辑器都觉得很蠢。




