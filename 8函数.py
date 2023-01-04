#要执行函数定义的特定任务，可调用该函数。
#需要在程序中多次执行同一项任务时，你无需反复编写完成该任务的代码，而只需调用执行该任务的函数，
#让Python运行其中的代码。你将发现，通过使用函数，程序的编写、阅读、测试和修复都将更容易。

def greet_user():
#定义了一个函数，函数名是greet_user
    """显示简单的问候语"""
    print("Hello!")
#函数的唯一功能是输出Hello
greet_user()
#这之后，只需要打出这个函数，python就会执行输出Hello一次

#只需稍作修改，就可以让函数greet_user()不仅向用户显示Hello!，还将用户的名字用作抬头。
#为此，可在函数定义def greet_user()的括号内添加username。
#通过在这里添加username，就可让函数接受你给username指定的任何值。
#现在，这个函数要求你调用它时给username指定一个值。调用greet_user()时，可将一个名字传递给它，
#如下所示：
def greet_user(username):
    """显示简单的问候语"""
    print("Hello, " + username.title() + "!")

greet_user('jesse')
#这个程序的执行步骤是，首先jesse存储在了变量username中，之后程序执行print中的输出语句
#前面定义函数greet_user()时，要求给变量username指定一个值。
#调用这个函数并提供这种信息（人名）时，它将打印相应的问候语。
#在函数greet_user()的定义中，变量username是一个形参——函数完成其工作所需的一项信息。
#在代码greet_user('jesse')中，值jesse是一个实参。
#实参是调用函数时传递给函数的信息。
#我们调用函数时，将要让函数使用的信息放在括号内。
#在greet_user('jesse')中，将实参jesse传递给了函数greet_user()，
#这个值被存储在形参username中。


#练习编写一个名为favorite_book()的函数，其中包含一个名为title的形参。
#这个函数打印一条消息，如One of my favorite books is Alice in Wonderland。
#调用这个函数，并将一本图书的名称作为实参传递给它。

def favorite_book(book_name):
    print("my favorite book is" + book_name)

favorite_book("1234")


#传递实参
#鉴于函数定义中可能包含多个形参，因此函数调用中也可能包含多个实参。
#向函数传递实参的方式很多，可使用位置实参，这要求实参的顺序与形参的顺序相同；
#也可使用关键字实参，其中每个实参都由变量名和值组成；还可使用列表和字典。
#下面来依次介绍这些方式。

#位置实参
#你调用函数时，Python必须将函数调用中的每个实参都关联到函数定义中的一个形参。
#为此，最简单的关联方式是基于实参的顺序。
#这种关联方式被称为位置实参。

def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
#这里的animal_type,pet_name就是位置形参
#使用位置实参来调用函数时，如果实参的顺序不正确，结果可能出乎意料

#关键字实参
#关键字实参是传递给函数的名称—值对。
#你直接在实参中将名称和值关联起来了，因此向函数传递实参时不会混淆
#不会得到名为Hamster的harry这样的结果。
#关键字实参让你无需考虑函数调用中的实参顺序，还清楚地指出了函数调用中各个值的用途。

def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name='harry',animal_type='hamster')

#使用关键字实参时，务必准确地指定函数定义中的形参名。


#默认值
#编写函数时，可给每个形参指定默认值。
#在调用函数中给形参提供了实参时，Python将使用指定的实参值；
#否则，将使用形参的默认值。
#因此，给形参指定默认值后，可在函数调用中省略相应的实参。
#使用默认值可简化函数调用，还可清楚地指出函数的典型用法。

def describe_pet(pet_name, animal_type='dog'):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name='willie')
describe_pet(pet_name='willi')

#请注意，在这个函数的定义中，修改了形参的排列顺序。
#由于给animal_type指定了默认值，无需通过实参来指定动物类型，
#因此在函数调用中只包含一个实参——宠物的名字。
#然而，Python依然将这个实参视为位置实参，
#因此如果函数调用中只包含宠物的名字，这个实参将关联到函数定义中的第一个形参。
#这就是需要将pet_name放在形参列表开头的原因所在。
#如果在调用的时候，仍然指名了第二个形参所对应的实参，那么Python将按照指名去输出，而不是默认值

#使用默认值时，在形参列表中必须先列出没有默认值的形参，再列出有默认值的形参。
#这让Python依然能够正确地解读位置实参


#返回值
#函数并非总是直接显示输出，相反，它可以处理一些数据，并返回一个或一组值。
#函数返回的值被称为返回值。
#在函数中，可使用return语句将值返回到调用函数的代码行。
#返回值让你能够将程序的大部分繁重工作移到函数中去完成，从而简化主程序。

def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
#我们首先定义一个函数
#这个函数的功能是根据用户输入的姓和名最终整合到完整的首字母大写的名字，然后将这个fullname作为结果
#这其中，体现返回值的一步在return语句上


#让实参变得可选
#背景：在使用函数的时候，有些形参虽然设置了，但用户却没有对应的实参，比如一般人都不会有中间名
#但显然，设置函数的时候，我们需要保证没有中间名的人也能够通过函数输出
#因此，我们需要对函数进行调整，让其在部分实参选填的情况下也能正常输出

def get_formatted_name(first_name, last_name, middle_name=''):
    """返回整洁的姓名"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
#上述代码，利用中间值默认值为一个空格，实现了中间名的可选填正常输出

#返回字典
#函数可以返回任何类型的值，包括列表和字典等较为复杂的数据结构
#下面的函数接受姓名的组成部分，并返回一个表示人的字典
def build_person(first_name, last_name):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)
#运行的结果，字典被作为结果输出了


#结合函数和while循环
def get_formatted_name(first_name,last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()
#请用户提供一系列输入时，我们可以用break语句实现轻松的退出

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")



 



