'''
1、写入CSV文件
   writerow([row_data]):一次写入一行数据
   writerows([row_data],[row_data],[row_data],...):一次写入多行数据
'''

#将用户信息写入到CSV文件中
import csv
#用户信息列表，嵌套列表内的每一个小列表是一行数据
#datas=[["name","age"],["zhangsan",20],["lisi",30]]  #嵌套列表内的第一个列表是标题
# with open("./user_info.csv","w") as f:
#     #writer函数会返回一个writer对象，通过writer对象向csv文件写数据
#     w=csv.writer(f)
#     # #循环遍历列表，一次写入一行数据
#     # for row in datas:
#     #     w.writerow(row)
#     #使用writerows方法一次性地将数据写入CSV文件
#     w.writerows(datas)

'''
2、读取CSV文件
   reader()方法：该方法会根据打开的文件对象返回一个可迭代的对象，然后遍历这个对象读取CSV文件中的每一行数据
'''
#读取当前运行的程序文件所在路径下的user_info.csv文件
with open("./user_info.csv","r",encoding='utf-8')as f:
    r=csv.reader(f) #返回一个reader可迭代对象
    for row in r:
        print(row) #row是一个列表
        print(row[0])  #通过索引获取列表中元素
        print(row[1])
        print("------------------")