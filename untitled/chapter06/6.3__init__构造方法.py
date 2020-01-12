'''
#在类中定义构造方法
class Dog:
    #构造方法
    def __init__(self):  #程序自动调用该构造方法
        print("执行了构造方法，正在初始化.....")
    def eat(self):
        print("正在啃骨头。。。")
    def drink(self):
        print("正在喝水。。。")
    def run(self):
        print("摇着尾巴奔跑！")

#创建对象
wangcai=Dog()
wangcai.eat()
wangcai.drink()
wangcai.run()
'''

#通过__init__构造方法设置小狗的对象属性
class Dog:
    #通过对象方法设置对象的品种和性别属性
    def __init__(self,v,g):
        print("开始初始化！")
        self.variety=v  #self.属性名=属性值
        self.gender=g
        print("初始化结束!")
#创建对象，传入旺财的品种是金毛，性别是雄性
wangcai=Dog("金毛","雄性")
#动态添加了name、age两个属性
wangcai.name="旺财"
wangcai.age=1
print("小狗的名字：{}，年龄：{}岁".format(wangcai.name,wangcai.age))
print("旺财的品种：{}".format(wangcai.variety))#通过“对象变量.属性名”的方式获取对象属性值
print("旺财的性别：{}".format(wangcai.gender))

tuofu=Dog("泰迪","雌性")
print("托福的品种：{}".format(tuofu.variety))#通过“对象变量.属性名”的方式获取对象属性值
print("托福的性别：{}".format(tuofu.gender))

