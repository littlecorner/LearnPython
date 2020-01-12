#想在自己写的代码中遇到问题时也抛出异常，使用raise语句

def div(a,b):
    if b==0:
        raise ZeroDivisionError("异常原因：除法运算，除数不能为0！")
    else:
        return a/b
div(2,0)