#捕获全部异常
try:
    #读取一个不存在的文件，将产出FileNotFoundError异常
    open("test.txt")
    #打印一个不存在的变量，将产生NameError异常
    print(num)
except NameError as err: #只捕获NameError，没有捕获FileNotFoundError
    print("捕获到了异常：",err)
except Exception as err_all:  #捕获所有可能发生的异常
    print("捕获到了全部异常：",err_all)

