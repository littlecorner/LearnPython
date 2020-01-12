#对程序中可能发生的异常进行预处理的过程就是异常处理

'''
#打开一个不存在的文件，发生异常 FileNotFoundError: [Errno 2] No such file or directory: 'test.txt'
file= open("test.txt")
print(file.read())
file.close()
print("文件读取结束!")

'''

#捕获异常
print("准备打开一个文件......")
try:
    open("test.txt")
    print("打开文件成功！")
except FileNotFoundError as err:
    print("捕获到了异常，文件不存在！",err)
print("程序即将结束！")