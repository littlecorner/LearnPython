#重写：在子类中定义与父类同名的方法
#子类Dog重写父类Animal的run()方法

#动物类
class Animal:
    def __init__(self):
        print("******Animal初始化******")
    def eat(self):
        print("----吃----")
    def drink(self):
        print("----喝----")
    def run(self):
        print("----跑----")

#狗类
class Dog(Animal):
    def __init__(self,name):
        self.name=name
        print("我的名字是：{}".format(self.name))
    #重写父类run()方法
    def run(self):
        print("摇着尾巴奔跑！")

#猫类
class Cat(Animal):
    def __init__(self,name):
        self.name=name
        print("我的名字是：{}".format(self.name))

animal=Animal()   #父类对象，调用父类中的run()方法
animal.run()

wangcai=Dog("旺财")
wangcai.run()    #调用了Dog类重写父类的run()方法

tom=Cat("汤姆")
tom.run()    #Cat类没有重写父类Animal的run()方法，所以tom调用了继承自父类Animal类的run()方法