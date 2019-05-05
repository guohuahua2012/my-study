import configparser #导入configparser模块

# 实例化cf
cf = configparser.ConfigParser()
# 读取config.ini文件
cf.read('config.ini')

# sections()方法：读取config.ini文件中的section的值
sections = cf.sections()

# options()方法：读取config.ini文件中该section下所有的option，即key的值
# for i in sections:
#     print(i)
#     print(cf.options(i))

# items()方法：读取config.ini文件中section，以键值对的形式输出key，value
# for i in sections:
#     print(i)
#     print(cf.items(i))

# get(section, option):读取指定section下面的option的值（可以理解成，读取具体某个group下面指定key的值）
for i in sections:
    #print(i)
    x = cf.options(i)
    #print(x)
    for j in x:
        #print(j)
        y = cf.get(i,j)
        print("{0}={1}".format(j,y))





