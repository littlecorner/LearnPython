'''
文件管理相关的操作需要引入python内置的os模块，使用“import os”方式引入

'''

import os

'''
1、rename(oldfile,newfile)函数：对文件或者文件夹重命名
'''
#os.rename("test.txt","测试.txt")

'''
2、remove(path)函数：删除指定文件
'''
#os.remove("测试.txt")

'''
3、mkdir(path)函数：在指定的路径下创建新文件夹
'''
#os.mkdir("d://testdir")

'''
4、getcwd()函数：获取程序运行的绝对路径
'''
print(os.getcwd())

'''
5、listdir(path)函数：获取指定路径下的文件列表
'''
# lsdir=os.listdir("./")
# print(lsdir)

'''
6、rmdir(path)函数：删除指定路径下的空文件夹
'''
os.rmdir("./datas")