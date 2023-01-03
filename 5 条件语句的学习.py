#if 条件语句 会根据是否满足if后的约束条件来决定后续的执行方案
things = ['audio', 'video', 'music','record','book']
for thing in things:
    if thing == 'music':
        print(thing.upper())
    else:
        print(thing.lower())

#使用and和or可以在一个if语句中使用多个约束条件
#需要注意的是，and所连接的所有条件必须全部得到满足，语句才会按照ture的结果去执行
#而or所连接的所有条件只需要满足其中一个，语句就会按照true去执行
#为了增强可读性，存在多个约束条件条件可以用括号()包括每个约束条件
things = ['audio', 'video', 'music','record','book']
for thing in things:
    if (thing == 'music') or (thing == 'record'):
        print(thing.upper())
    else:
        print(thing.lower())

#检查特定元素在列表中的存在性
#使用in和not in 来判断元素在列表中存在还是不存在
things = ['audio', 'video', 'music','record','book']
for thing in things:
    if 'game' in things:
        print(thing.upper())
    if 'game' not in things:
        print(thing.title())
    else:
        print(thing)

#上述代码中，第二个if也可以写成elif，但二者的效果不完全相同
things = ['audio', 'video', 'music','record','book']
for thing in things:
    if 'game' in things:
        print(thing.upper())
    elif 'game' not in things:
        print(thing.title())
    else:
        print(thing)

#elif.前段的el代表了对先前约束条件的否定，后段的if则是新建另一个约束条件
things = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
for thing in things:
    if thing <= 3:
        print("aaaaa")
    elif thing <=16:
        #这句话限定的条件范围是大于3小于等于16
        print("bbbbb")
    else:
        print(thing)

#看下面一行代码，学会从布尔值的角度加深对if等条件语句的理解
requests = []
if requests:
#这里看似并没有添加任何条件，但实际上，在if语句中将列表名用在表达式中时，Python将在
#列表至少包含一个元素时返回True，并在列表为空的时候返回False
    for request in requests:
        print(1)
else:
    print(123)

#两个列表之间的条件语句案例
requests = [2,4,6,8]
available_requests = [1,2,3,4,5,6,7,8,9]
for request in requests:
    if request in available_requests:
        print(request)
    else:
        print(0)






































































