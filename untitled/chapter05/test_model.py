def test_info():
    #打印__name__变量的值

    print("test_info正在运行，__name__值={}".format(__name__))
#函数调用
#test_info()

#把不希望在被引入时执行的代码放在if条件判断的代码块中
if __name__=="__main__":
    test_info()
