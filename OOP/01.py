'''
定义一个学生类，用来形容学生

'''
# 定义一个空的类
class Student():
    # 一个空类，pass 代表直接跳过
    # 此处pass 必须有
    pass


# 定义一个对象
# mingyue 就是一个对象，属于Student()类中的一个个体
mingyue = Student()


# 在定义一个类，用来描述听python的学生
class PythonStudent(): # class关键字 + PythonStudent() 类名单词首字母大写 + 冒号：
    # 用None 给不确定的值赋值
    # 定义变量的属性名及赋值
    name = None
    age = 18
    course = "Python"

    # 需要注意
    # 1. def doHomework的缩进层级，小于class的缩进层级，与变量的缩进平级
    # 2. 系统默认有一个self参数
    def doHomework(self):
        print("I 在做作业")

        # 推荐在函数末尾使用return语句
        return None

# 实例化一个叫yueyue的学生，是一个具体的人
yueyue = PythonStudent()

print(yueyue.name)
print(yueyue.age)
print(yueyue.course)
# 注意成员函数的调用没有传递进入参数
yueyue.doHomework()

# 打印查看PythonStudent类内所有的成员
print(PythonStudent.__dict__)

import random
print(random.randint(0,9999999999999999999))



# 定义一个类
class A():
    # 定义属性
    name = "chunhua"
    age = 18

    def say(self):
        self.name = "guochunhua"
        self.age = 30


# 此案例说明
'''
类实例的属性（A.name）和其对象实例的属性（a.name），如果不进行对象的实例属性赋值（a.name！= "xxx"）,
则两者指向的为同一个变量(id值不变)
'''

# 此时，A称为类的实例
print(A.name)
print(A.age)

print("-" * 30)

# id 可以鉴别两个变量 是否为同一个变量
print(id(A.name))
print(id(A.age))

print("-" * 30)
# 定义一个对象
a = A()
# 此时，a称为对象的实例，借用了A()类实例的属性
print(a.name)
print(a.age)
print(id(a.name))
print(id(a.age))

'''
类实例的属性（A.name）和其对象实例的属性（a.name），如果对对象的实例属性进行赋值（a.name = "xxx"）,
则两者指向的内容不是同一个变量了（id值已变化）
'''
# 此时，A称为类的实例
print("*" * 30)
print(A.name)
print(A.age)

print("-" * 30)

# id 可以鉴别一个变量与另外一个变量 是否为同一个变量
print(id(A.name))
print(id(A.age))
# 查看A内所有的属性值
print(A.__dict__)
print(a.__dict__)

print("分隔符----" * 10)
# 定义一个对象
a = A()
# 进行对象实例赋值
a.name = "huihui" # 等价于 self.name = "huihui"
a.age = 20        # 等价于 self.age = 20
# 打印查看对象实例赋值后，对象实例的成员
print(a.__dict__)

print(a.name)
print(a.age)
print(id(a.name))
print(id(a.age))


# self 使用
print("this is self ------------------------")
class StudentA():
    name = "chunhua"
    age = 18

    def myInfo(self):
        self.name = "huahua"
        self.age = 200
        print("My name is {0}".format(self.name))
        print("My age is {0}".format(self.age))

my = StudentA()
# 对象my把自己作为第一个参数传入函数myInfo()中
# 即self.name 等价于 my.name ; self.age 等价于 my.age
my.myInfo()


# 有self 与 没有self的区别
print("有self 与 没有self的区别示例")
class Teacher():
    name = "laoshi"
    age = 20

    # 定义一个非绑定类的方法
    def heSelf(self):
        self.name = "liudana"
        self.age = 30
        print("My name is {0}".format(self.name))
        print("My age is {0}".format(self.age))
    # 定义一个绑定类的方法
    def heHe():
        print("他说他是python老司机...")

ta = Teacher()
# 调用非绑定类函数使用对象名
# 对象ta会作为参数传入函数中
ta.heSelf()

# 调用绑定类函数使用类名
# 此时类名不会作为参数传入函数中
Teacher.heHe()


# 使用类 访问绑定类方法，且方法中需要访问类中的成员
print("使用类 访问绑定类方法，且方法中需要访问类中的成员，使用 __class__.方法的示例------------------------------")

class MyInfo():
    name = "过去"
    age = 18

    def nowSelf(self):
        self.name = "现在"
        self.age = 30
        print("我{0}很年轻{1}，做错很多事，很不开心！！！".format(__class__.name, __class__.age))
        print("我{0}年纪大了，已经{1}，但很开心。。。".format(self.name, self.age))

    def nowBefor():
        print("{0}的都已经成为历史，{0}的算了。。。".format(__class__.name))
        print("其实我还很年轻，我现在心态是{0}岁。。。".format(__class__.age))

wo = MyInfo()
wo.nowSelf()
# 访问绑定类的方法时，使用对象名.函数名 访问时出错。
# wo.nowBefor()
# 访问绑定类方法时 需使用类名.函数名 访问。

MyInfo.nowBefor()



# self 案例
class B():
    name = "学生"
    age = 18

    # 构造函数
    def __init__(self):
        self.name = "程序员"
        self.age = 30

    def say(self):
        print(self.name)
        print(self.age)

class C():
    name = "C++"
    age = 35

# 实例化
a = B()
# 此时，a为对象实例 访问非绑定类的方法时，系统会默认把a作为第一参数传入say函数
a.say()

# 此时，B为类实例，访问非绑定类的方法时，需要手动将对象a作为参数传入say函数，即self被a替换
B.say(a)

# 此时，把B作为参数传入say函数，即self被B替换了，即调用B类中的 name 和 age 成员（前提条件时，B类中必须存在name和age属性成员，否则报错）
B.say(B)
# 同理，可以把类C 作为参数传入say函数，同样C类中也必须存在name和age属性成员，否则报错
B.say(C)

# 以上代码 利用了鸭子模型（看起来像鸭子、具有鸭子的属性<有翅膀、会游泳、嘎嘎嘎叫...>，就认为你是鸭子）
# 同理以上代码中使用的 B类和 C类 不管是否为同一类型，只要存在函数say中所需要的属性<name, age>,即认为B和C是同一类



# 私有变量示例

class Person():
    # name 是公有的成员
    name = "chunhua"
    # __age 就是私有成员，在age前面添加两个下划线即可
    __age = 18

    _stature = "slender"

p = Person()
# name 作为公有变量，在外部访问，没毛病...
print(p.name)

# __age 做为私有变量，此时在外部方式，则报错。。。'object has no attribute'
# print(p.__age)
# name mangling 技术
# 查看类内所有成员
print(Person.__dict__)
p._Person__age = 180
# private 私有
print(p._Person__age)
print(Person.__dict__)

# protected 受保护的
print(Person.__dict__)
p._stature = "tall"
print(p._stature)
print(Person.__dict__)







