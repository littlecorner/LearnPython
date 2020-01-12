'''

#子类GoldenDog通过 父类名.方法名(self[,参数列表])  的方式调用父类Dog中的hand()方法
#定义Animal动物类
class Animal:
    #定义动物类具有的一些行为
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
        print("******握手*******")

class GoldenDog(Dog):
    def guide(self):
        print(">>>>>我能导航<<<<<")
        print("提示：想要我导航，请先跟我握手！")
        #通过  父类名.方法名   调用父类Dog的hand方法
        Dog.hand(self)

duoduo=GoldenDog()
duoduo.guide()

'''
#子类GoldenDog通过 super().方法名  的方式调用父类Dog中的hand()方法
