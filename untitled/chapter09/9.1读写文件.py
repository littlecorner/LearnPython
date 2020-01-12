'''
1、打开文件
   open函数：三种常用模式   只读模式（默认，使用字母 r 表示）：只用于读取文件内容，不能向文件中写入数据
                           只写模式（使用字母 w 表示）：用于将数据覆盖写入到文件中
                           追加模式（使用字母 a 表示）：用于将数据追加写入到文件的末尾
   打开一个不存在的文件时：  只读模式会报FileNotFoundError: [Errno 2] No such file or directory: 'test.txt'
                            只写和追加两种模式都会创建一个新的空文件
   打开一个存在的文件时：    这三种模式都会正常打开一个文件，open函数会返回一个文件对象，通过操作这个文件对象，读取文件内容或者向文件写入数据
'''
#使用只读模式打开一个不存在的文件
#f = open("test.txt","r")  #程序文件所在路径下没有test.txt文件

#使用只写模式打开一个不存在的文件
#通过只写模式打开一个不存在的文件，如果没有指定文件路径，那么会在程序执行的当前路径下创建该文件
#f = open("test.txt","w")


'''
2、写文件
   write()方法：将一个字符串数据写入到文件中，不会自动换行
                b执行的内容将会覆盖a执行的内容
                c使用了追加模式打开文件，则在文件末尾追加数据而不是覆盖原有的内容
   writelines()方法： 将一个序列中的多个字符串一次性写入到文件中
   close()方法：写完文件之后，文件对象调用close()方法关闭文件
'''
#write()方法

#a、第一次执行
# f = open("stunames.txt","w")
# #写入三个学生的名字
# f.write("Tom")
# f.write("David")
# f.write("Carl")

#b、第二次执行
# f = open("stunames.txt","w",encoding='utf-8')
# #写入三个学生的名字
# f.write("孔")
# f.write("灿")
# f.write("灿\n")
#
# #c、第二、三次执行
# f = open("stunames.txt","a",encoding='utf-8')
# f.write("你\n")
# f.write("真\n")
# f.write("棒\n")

#writelines()方法

#一次写入多个字符串到文件中
# f = open("stunames.txt","w",encoding='utf-8')
# f.writelines(["张三\n","李四\n","王五\n"])
# f.close()#关闭文件

#使用with关键字安全打开关闭文件
#open()函数打开文件返回的文件对象通过 as 命名为 f，通过文件对象 f 操作文件，操作完文件程序自动关闭文件
# with open("stunames.txt","w",encoding='utf-8') as f:
#     f.writelines(["张三\n","李四\n","王五\n"])

'''
3、读文件
   read()方法：一次性从文件中读取出所有文件内容
   readlines()方法：按照行的方式把整个文件中的内容一次全部读取出来，返回结果的是一个列表，文件中的一行数据就是列表中的一个元素
                    由于文件中每行末尾包含一个不可见的换行符“\n”，所以列表中每一个元素的最后也包含一个换行符“\n”
'''

# #使用read()方法读取stuname文件中所有学生名字
# with open("stunames.txt","r",encoding='utf-8') as f:
#     data=f.read()
#    print(data)

#使用readlines()方法按行读取stunames文件中所有学生名字
with open("stunames.txt","r",encoding='utf-8') as f:
    lines=f.readlines()
    print(lines)
    #循环遍历lines，打印每行内容
    for i in range(0,len(lines)):
        print("第{}行：{}".format(i,lines[i]),end="")