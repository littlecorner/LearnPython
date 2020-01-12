'''
1、now()方法
   该方法返回值的默认格式是：YYYY-MM-DD HH：MM：SS.mmmmmm
   datetime.datetime.now()方法用于获取程序运行的当前日期和时间
   第一个datetime：模块名称
   第二个datetime：指的是在datetime模块中定义的datetime类，在这个datetime中定义了日期和时间相关的处理方法
'''

import datetime
import time
# #1.获取当前日期时间
# current_time=datetime.datetime.now()
# print("默认格式：{}".format(current_time))
#
# #2.在datetime类中内置了可以非常方便地获取now()方法返回值中指定日期时间的方法
# print("当前时间：",current_time)
# print("year:",current_time.year)
# print("month:",current_time.month)
# print("day:",current_time.day)
# print("hour:",current_time.hour)
# print("minute:",current_time.minute)


# #3.计算时间差值
# start_time=datetime.datetime.now()
# print("开始时间：",start_time)
# #让程序睡眠2秒钟
# time.sleep(2)
# end_time=datetime.datetime.now()
# print("结束时间：",end_time)
# print("时间差：{}秒".format(end_time.second-start_time.second))

'''
2、strftime(fmt)方法：按照自定义的格式化方式对日期和时间进行格式化
   函数需要传入一个字符串类型的fmt参数，该参数是由时间格式化符号组成的
   
'''

# #自定义格式化当前日期时间
# format_time=datetime.datetime.now().strftime("%Y/%m/%d/ %H:%M:%S")
# print("自定义格式：{}".format(format_time))

'''
3、fromtimestamp(timestamp)方法：对传入的时间戳timestamp参数以日期时间的形式进行格式化
   该方法返回值的默认格式是：YYYY-MM-DD HH：MM：SS.mmmmmm
   还可以调用strftime(timestamp)方法将返回值以自定义的日期时间形式进行格式化
'''

# #将时间戳格式化为日期时间
# ts=time.time()  #获取当前时间戳
# print("默认格式化：",datetime.datetime.fromtimestamp(ts))  #默认格式化
#
# #自定义格式化
# print("自定义格式化:",datetime.datetime.fromtimestamp(ts).strftime("%Y/%m/%d/ %H:%M:%S"))

'''
4、timedelta类：datetime模块内置的时间间隔类，
   如：datetime.timedelta(days=1)表示创建一个1天时间间隔的对象
'''

#计算昨天的日期   方法：昨天的日期 = 今天的日期 - 1天的时间间隔
today = datetime.datetime.today()
print("今天的日期：{}".format(today.strftime("%Y-%m-%d")))
days = datetime.timedelta(days=1)
yesterday = today-days  #今天减去时间间隔得到昨天的日期时间
print("昨天的日期：{}".format(yesterday.strftime("%Y-%m-%d")))
