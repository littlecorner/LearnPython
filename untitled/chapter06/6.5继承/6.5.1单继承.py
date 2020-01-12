'''

#单继承：子类只继承自一个父类
#定义Animal动物类
class Animal:
    #定义动物类具有的一些行为
    def eat(self):
        print("----吃----")
    def drink(self):
        print("----喝----")
    def run(self):
        print("----跑----")

#定义子类Dog继承父类Animal
class Dog(Animal):
    #狗类除了继承父类Animal具备的行为，它还会握手
    def hand(self):
        print("******汪汪汪*******")

#定义子类GoldenDog金毛继承父类Dog
class GoldenDog(Dog):
    #金毛能够作为导盲犬，具有导航功能
    def guide(self):
        print("+++++我能导航+++++")

wangcai=Dog()
#子类Dog中没有定义eat(),drink(),run()方法
wangcai.eat()
wangcai.drink()
wangcai.run()
wangcai.hand()
print("==============")

duoduo=GoldenDog()
duoduo.eat()
duoduo.hand()
duoduo.guide()
'''

#继承中构造方法的使用
class Animal:
    #定义构造方法
    def __init__(self):
        print("Animal初始化！")
    def eat(self):
        print("----吃----")
    def drink(self):
        print("----喝----")
    def run(self):
        print("----跑----")

class Dog(Animal):
    #定义构造方法
    def __init__(self):
        print("Dog初始化！")

    def hand(self):
        print("******汪汪汪*******")

class GoldenDog(Dog):
    def guide(self):
        print("+++++我能导航+++++")

#GoldenDog中没有定义构造方法，创建GoldenDog对象，会自动调用父类Dog的init构造方法
duoduo=GoldenDog()
duoduo.guide()
#Dog中定义了构造方法，创建Dog对象时，只会调用自己的构造方法初始化
wangcai=Dog()
wangcai.hand()
