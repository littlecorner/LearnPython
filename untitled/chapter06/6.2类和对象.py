#定义一个小狗类
#小狗具备 的行为时吃饭、喝水、奔跑
class Dog:
    def eat (self):
        print("正在啃骨头。。。")
    def drink(self):
        print("正在喝水。。。。")
    def run(self):
        print("摇着尾巴奔跑!")

#根据Dog类创建出了一个对象并赋值给了一个变量wangcai
print("------hello旺财-------")
wangcai=Dog()

#调用对象具备的行为（方法）
wangcai.eat()
wangcai.drink()
wangcai.run()

print("------hello托福-------")
tuofu=Dog()
tuofu.eat()
tuofu.drink()
tuofu.run()

print("-------对比两只小狗的id------")
print("旺财的id：{}".format(id(wangcai))) #id函数获取一个对象的内存地址
print("托福的id：{}".format(id(tuofu)))