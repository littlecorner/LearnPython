#多继承：一个子类可以继承多个父类，这样这个类就能够同时具备多个父类的非私有方法
#多继承的定义方式：在类名后的括号中添加需要继承的多个类名，不同的父类之间用逗号隔开
'''
在多继承中，如果不同的父类具有同名的方法，当子类对象未指定调用哪个父类的同名方法时，
那么查找调用方法的顺序是：
在小括号内继承的多个父类中，按照从左到右的顺序查找父类中的方法，第一个匹配成功方法名的父类方法将被调用

'''

#人工智能类
class AI:
    #人脸识别
    def face_recognition(self):
        print("----人脸识别----")
    #数据处理
    def data_handle(self):
        print("AI数据处理")

#大数据类
class BigData:
    #数据分析
    def data_analysis(self):
        print("-----数据分析----")
    #数据处理
    def data_handle(self):
        print("BigData数据处理")

#python语言类继承 AI 和 BigData
class PythonLanguage(AI,BigData): #多继承
    def operation(self):
        print("+++++运维+++++")

py= PythonLanguage()
#分别调用两个父类的方法
# py.face_recognition()
# py.data_analysis()
# py.operation()

#通过类内置的__mro__属性可以查看方法解析（搜索）顺序
print(PythonLanguage.__mro__)
#调用不同父类中同名的方法
py.data_handle()
