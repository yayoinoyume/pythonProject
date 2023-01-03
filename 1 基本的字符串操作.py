name = "Jack "
name2 = "peter"
full = name + " " + name2
print(full)
print(full.upper())
print(full.lower())
print(full.capitalize())

first_name = "Ada"
last_name = "Jack"

print("Hello, " + first_name + " "  + last_name +",nice to see you!")

print("Languages:\n\tPython\n\tC++\n\tC\n\tJavascript")
#\n 换行
#\t 添加制表符，相当于按一次tab


name = "     javascript   a    "
print(name.rstrip())
print(name.lstrip())
print(name.strip())
print("".join(name.split()))
print(name.replace(" " , ""))
#rstrip去除右侧的空格，lstrip去除左边的空格，strip去除左右两边的空格
#如果想要去除中间部分的空格，可以用join和split组合的方法，也可以用replace的办法。
#其中，print("",join(name.split()))语句中，spliit是把name这个字符串中的javascript和a切割，
#变成列表里面的两个元素，join是在这个列表创建之后，有序取出列表中的元素，
#再把他们按照一定规律连接组合成一个字符串，这里的规律，就是连接方式，也即第一个""的作用
#""中的内容，代表了用什么东西连接，如果什么都不写，就是直接连接，而如果写成"1"就是javascript1a
#然而，这样的删除空格只是在输出的时候暂时的删除，如果想要永久去除文本中的空格，必须要将去除空格后的
#值重新存储到变量中。

#练习2-3 将用户姓名存到一个变量之中，并向该用户显示一条消息
name = "弥生の夢"
print("Hello!" + name + "welcome to the world of pythons!")

#练习2-4调整一个名字的大小写，并将其中一个人名存储到一个变量当中，再以小写，大写，首字母大写显示
name1 = "Jack"
name2 = "Bob"
name3 = "Peter"
name4 = name3.upper()
print(name4)