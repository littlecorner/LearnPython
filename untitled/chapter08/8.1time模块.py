
'''
1、time函数
   调用time函数时，将会返回当前的时间戳，返回的时间戳是以秒为单位的浮点数
'''

import time
#获取当前时间戳
print(time.time())

'''
2、localtime（[seconds]）函数可以传入一个可选参数，可选参数是以秒为单位的时间戳
   a.如果不传入任何参数，则将当前时间戳转换成本地时间，返回一个time内置的struct_time元组
   b.如果传入时间戳作为参数，则将时间戳格式化为本地时间，返回一个struct_time元组
'''
#a.
# date_time=time.localtime()
# print(date_time)

# #b.
# #获取当前时间戳
# ts=time.time()
# #向localtime函数传入时间戳
# date_time=time.localtime(ts)
# print(date_time)
# #将指定时间戳转换成本地时间
# print(time.localtime(1578657353.3822222))

'''
3、strftime（fmt[,struct_time]）函数：可以按照自定义的格式化参数将时间格式化
   fmt：函数调用时传入的字符串类型的自定义格式化参数，它是由时间格式化符号表示的
   第二个参数struct_time元组是可选参数，不传入该参数表示将当前时间格式化
'''

# #自定义时间格式化
# #默认格式化当前时间
# #print(time.strftime("当前时间：%Y %m %d %H %M %S"))  #第一个参数中含有”当前时间：“汉字，故报错
# print(time.strftime("%Y-%m-%d %H:%M:%S"))  #将当前时间格式化
# #传入指定struct_time参数，对其格式化
# print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(1514829722)))    #将时间戳1514829722格式化

'''
4、strprime(date_time,format)函数：将一个格式化的时间字符串转换成struct_time元组
   第一个参数date_time：表示格式化时间字符串
   第二个参数format：表示时间格式化方式
'''

# time_tuple=time.strptime("2018-09-11 09:01:38","%Y-%m-%d %H:%M:%S")
# print(time_tuple)

'''
5、mktime（p_tuple）函数：将一个时间元组转换成一个浮点型时间戳
'''

#获取当前时间的时间戳
# ts=time.mktime(time.localtime())
# print(ts)


'''
6、sleep(seconds)函数：在程序运行过程中，让程序暂停运行，睡眠等待几分钟
'''

#计时器
for t in range(3,-1,-1): #range(start,end,step)
    print("倒计时：",t)
    if t!=0:
        time.sleep(1)
    else:
        print("go!")