#异常传递：从内部调用的函数把产生的异常传递给外部函数

def func1():
    print("-----test1-1------")
    #打印一个不存在的变量，产生异常，但是没有捕获
    print(num)
    print("-----test1-2------")

def func2():
    try:
        print("------test2-1------")
        #调用func1函数，捕获异常
        func1()
        print("------test2-2------")
    except Exception as err:
        print("捕获到了异常：",err)
        print("----test2-3------")
#调用func2函数
func2()
