#input()函数
#input()函数让程序暂时停止允许，并允许用户在此时向程序输入一些数据信息
name = input("please enter your name here:      ")
print(name)

#
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
#直接附加在what is your name 这句话后面
print("\nHello, " + name + "!")

#在使用输入函数的时候，用户输入的所有信息都会被默认以字符串的形式存储
#所以如果想要有效利用用户输入的信息，就必须将input函数获得的信息转换成有效的信息格式
#比如以下这个例子
age = input("How old are you? ")

#用户在此输入数字，比如21
#那么程序获取到的21是字符串格式的，它并不是数值，不可以参与如相加或比大小之类的数学操作
#这时候可以使用int()将输入的数据转化为数值
age1 = int(input("How old are you? "))
#也可以
age2 = input("How old are you? ")
int(age2)

#求模运算符
#%是求模运算符，它不会指出一个数是另一个数的多少倍
#而是指出一个数除以另一个数后的余数是多少
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")

#根据一个数能否被2整除，我们可以判断它是奇数还是偶数

#练习，一个数是否是10的整数倍
num = int(input("please give us a number"  ))
print(num % 10 == 0)



#while循环
#while循环是根据编写者设定的条件来判断是否进行下去的循环
#例如下面这段代码，设定循环是在程序记数到5之前一直记数
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

#让用户选择何时退出
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)

    print(message)
#这个程序的意思是，在用户输入quit之前，程序会一直输出prompt中的话
#而当用户输入quit后，程序会将quit再输出一遍
#可以利用If语句来消去退出时对quit的重复
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)
#阅读while循环时，应当先阅读其缩进的内容，理解是什么东西在循环
#比如上述，程序邀请用户输入message并复述这些东西，但当用户输入quit时，if条件没有触发，程序直接退出


#使用标志以及使用标志来退出循环

#在前一个示例中，我们让程序在满足指定条件时就执行特定的任务。
# 但在更复杂的程序中，很多不同的事件都会导致程序停止运行；在这种情况下，该怎么办呢？

#例如，在游戏中，多种事件都可能导致游戏结束，
#如玩家一艘飞船都没有了或要保护的城市都被摧毁了。
#导致程序结束的事件有很多时，如果在一条while语句中检查所有这些条件，将既复杂又困难。
#在要求很多条件都满足才继续运行的程序中，可定义一个变量，用于判断整个程序是否处于活动状态。
#这个变量被称为标志，充当了程序的交通信号灯。
#你可让程序在标志为True时继续运行，并在任何事件导致标志的值为False时让程序停止运行。
#这样，在while语句中就只需检查一个条件——标志的当前值是否为True
#并将所有测试（是否发生了应将标志设置为False的事件）都放在其他地方，从而让程序变得更为整洁。

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)
#我们将变量active设置成了True，让程序最初处于活动状态。
#这样做简化了while语句，因为不需要在其中做任何比较——相关的逻辑由程序的其他部分处理。
#只要变量active为True，循环就将继续运行。
#在while循环中，我们在用户输入后使用一条if语句来检查变量message的值。
#如果用户输入的是quit，我们就将变量active设置为False，这将导致while循环不再继续执行。
#如果用户输入的不是quit，我们就将输入作为一条消息打印出来。
#这个程序的输出与前一个示例相同。
#在前一个示例中，我们将条件测试直接放在了while语句中，
#而在这个程序中，我们使用了一个标志来指出程序是否处于活动状态，
#这样如果要添加测试（如elif语句）以检查是否发生了其他导致active变为False的事件，将很容易。
#在复杂的程序中，如很多事件都会导致程序停止运行的游戏中，标志很有用：
#在其中的任何一个事件导致活动标志变成False时，主游戏循环将退出，此时可显示一条游戏结束消息
#并让用户选择是否要重新玩。


#使用break来退出循环

#要立即退出while循环，不再运行循环中余下的代码，也不管条件测试的结果如何，可使用break语句。
#break语句用于控制程序流程，可使用它来控制哪些代码行将执行，哪些代码行不执行，
#从而让程序按你的要求执行你要执行的代码。
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")
#程序提示用户输入一个想去的地方并且为用户造句，但当用户输入quit后，程序执行break，终止运行

#事实上，在python的各种循环中都可以使用break语句，包括之前所学习的for循环
#这是之前的记数代码，需要注意的是，这个代码在数到10之前会把每一次数的数报出来
current_number = 1
while current_number <= 10:
    print(current_number)
    current_number += 1

#重置循环 continue
#要返回到循环开头，并根据条件测试结果决定是否继续执行循环，可使用continue语句
#它不像break语句那样不再执行余下的代码并退出整个循环。
#例如，来看一个从1数到10，但只打印其中奇数的循环：
current_number = 0
while current_number <= 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)
#在上述代码中，我们利用循环来记数，但只有当循环记数的数字为奇数时，代码才会把数字报出来
#当循环的数字为偶数的时候，代码会执行if下的continue语句
#让循环回到初始状态，而不执行print那部分的循环，从而实现偶数不输出

#每个while循环都必须有停止运行的途径，这样才不会没完没了地执行下去。
#要避免编写无限循环，务必对每个while循环进行测试，确保它按预期那样结束。
#如果你希望程序在用户输入特定值时结束，可运行程序并输入这样的值；
#如果在这种情况下程序没有结束，请检查程序处理这个值的方式，
#确认程序至少有一个这样的地方能让循环条件为False或让break语句得以执行。


#使用while循环来处理列表和字典
#到目前为止，我们每次都值处理了一项用户信息，获取用户的输入，再讲输入打印出来或者作出应答
#循环再次进行时，我们获悉另一个输入值并作出相应，然而，要记录大量用户的信息，需要在while循环中
#使用列表和字典
#for循环是一种遍历列表的有效方式，但在for循环中，不应该修改列表，否则将导致python难以跟踪其中的元素
#要在遍历列表的同时对其进行修改，可以使用while循环，通过将while循环同列表和字典结合起来使用
#可以收集，存储和组织大量输入，供以后的查看和显示

#在列表之间移动元素
#假设有一个列表，其中包含新注册但还未验证的网站用户；
#验证这些用户后，如何将他们移到另一个已验证用户列表中呢？
#一种办法是使用一个while循环，
#在验证用户的同时将其从未验证用户列表中提取出来，再将其加入到另一个已验证用户列表中。
#代码可能类似于下面这样：

# 首先，创建一个待验证用户列表
#  和一个用于存储已验证用户的空列表
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# 验证每个用户，直到没有未验证用户为止
#  将每个经过验证的列表都移到已验证用户列表中
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
#利用pop()将列表中的元素进行剪切，达到移动的效果
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

# 显示所有已验证的用户
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())


#删除包含特定值的所有列表元素
#在列表中，我们同过remove()来删除列表中的特定值，
#需要注意的是，这种方法仅仅在列表中被删除元素只出现了一次的时候才有效
#那么如何删除列表中所有包含特定值的元素呢，可以用while循环来不断执行删除，直到删除干净为止
#假设你有一个宠物列表，其中包含多个值为'cat'的元素。
#要删除所有这些元素，可不断运行一个while循环，直到列表中不再包含值cat，如下所示：
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)
#通过while，不断删除列表中的cat，直到删除干净后再次输出列表


#使用用户输入来填充字典
#可以使用while循环提示用户输入任意数量的信息，下面来创建一个调查程序，其中的循环
#每次执行时都会提示输入被调查者的名字和回答，我们将收集的数据存储在一个字典中
#以便将回答同被调查者关联起来

#创建一个空字典
responses = {}

# 设置一个标志，指出调查是否继续
polling_active = True

while polling_active:
    # 提示输入被调查者的名字和回答
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # 将上述获得的用户的name作为键，response作为值存储在字典中
    responses[name] = response

    # 看看是否还有人要参与调查
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False

# 调查结束，显示结果
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")

#下面咱来仿写一个体会一下
#一个简单的选课小程序，用户输入用户名和想选的课程，系统最后输出选课结果
#首先，创建一个空字典
lesson = {}
#设置并激活标志

active = True
while active:
    name = input("please tell us your name"  )
    choice = input("what class would you like to choose?")
    lesson[name] = choice

    repeat = input("enter quit to quit")

    if repeat == "quit":
        active = False

for name,choice in lesson.items():
    print(name + ": " + choice)

#练习1创建一个名为sandwich_orders的列表，在其中包含各种三明治的名字；
#再创建一个名为finished_sandwiches的空列表。
#遍历列表sandwich_orders，对于其中的每种三明治，都打印一条消息，
#如I made your tuna sandwich，并将其移到列表finished_sandwiches。
#所有三明治都制作好后，打印一条消息，将这些三明治列出来。

sandwich_orders = ['a','b','c','c','c','c']
finished_sandwiches = []
while sandwich_orders:
    finished_order = sandwich_orders.pop()

    print("I made your order"  + finished_order.title())
    finished_sandwiches.append(finished_order)

for finished_sandwich in finished_sandwiches:
    print(finished_sandwiches)

#练习2，删除干净c
sandwich_orders = ['a','b','c','c','c','c']
while "c" in sandwich_orders:
    sandwich_orders.remove("c")

for sandwich_order in sandwich_orders:
    print(sandwich_order)