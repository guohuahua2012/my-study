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

# id 可以鉴别一个变量与另外一个变量 是否为同一个变量
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

    def my_info(self):
        self.name = "huahua"
        self.age = 200
        print("My name is {0}".format(self.name))
        print("My age is {0}".format(self.age))

my = StudentA()
# 对象my把自己作为参数传入函数my_info()中
# 即self.name 等价于 my.name ; self.age 等价于 my.age
my.my_info()


# 有self 与 没有self的区别
print("有self 与 没有self的区别示例")
class Teacher():
    name = "laoshi"
    age = 20

    # 定义一个非绑定类的方法
    def he_self(self):
        self.name = "liudana"
        self.age = 30
        print("My name is {0}".format(self.name))
        print("My age is {0}".format(self.age))
    # 定义一个绑定类的方法
    def he_he():
        print("他说他是python老司机...")

ta = Teacher()
# 调用非绑定类函数使用对象名
# 对象ta会作为参数传入函数中
ta.he_self()

# 调用绑定类函数使用类名
# 此时类名不会作为参数传入函数中
Teacher.he_he()

# 私有变量案例
class Person():
    name = "Guochunhua"
    __age = 30

p = Person()
# name是共有变量
print(p.name)
print(Person.__dict__)
# __age 是私有变量
#可以使用对象._classname__attributename访问
print(p._Person__age)
