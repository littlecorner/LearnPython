#具有私有权限的属性和方法在类内部是可以被访问的，在类外部无法访问私有属性和方法
class Dog:
    def __init__(self,n):
        self.name = n
        self.__age = 1 #私有属性

    #私有方法，用于设置年龄
    def __setAge(self,a):
        self.__age=a
    #设置名字和年龄属性
    def setInfo(self,name,age):
        #如果传入的名字不是空字符串，则给对象设置新的名字
        if name!="":
            self.name=name
        if age>0 and age<=20:
            #调用私有方法设置年龄
            self.__setAge(age)
        else:
            print("设置年龄失败，非法年龄！")

    def getInfo(self):
         #在函数内访问私有属性"__age"
        print("我的名字是：{}，我现在{}岁！".format(self.name,self.__age))

wangcai=Dog("旺财")
wangcai.getInfo()
print("我长大了！")

#给旺财设置新的年龄
wangcai.setInfo("",10)
wangcai.getInfo()

#在类外部无法访问私有属性和方法 故报错！！！！
#print("我的名字是：{}，我{}岁了！".format(wangcai.name,wangcai.__age))
#wangcai.__setAge(10)