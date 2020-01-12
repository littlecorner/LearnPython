#要使用try...except捕获多个异常，只需要把要捕获的异常的类名存储到except的元组中。
#在程序运行过程中只要发生元组中列举的任何一个异常，都会被捕获并异常处理。
#我们还可以使用as关键字对可能发生的异常重命名

try:
    #打印一个不存在的变量，将产生NameError异常，
    #捕获到了异常之后，没有向下执行open("test.txt")语句，而是进入except的代码块中处理异常
    print(num)
    #读取一个不存在的文件，将产生FileNotFoundError异常
    open("test.txt")
except(NameError,FileNotFoundError) as err:
    print("捕获到了异常！",err)
print("程序即将结束！")
