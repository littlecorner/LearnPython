#产生并且捕获了异常，执行finally语句
try:
    f=open("test.txt")
    print("打印文件内容！")
# except FileNotFoundError as err:
#     print("捕获到了异常！",err)
finally:
    print("关闭连接！")

#没有异常，执行finally语句
# try:
#     num= "hello python!"
#     print(num)
# finally:
#     print("关闭连接！")
#