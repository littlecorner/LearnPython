import urllib
import urllib.request
import urllib.parse
import urllib.response
'''
使用urlopen()函数发送HTTP请求时，不传入data参数表示以GET方式发送请求，传入data参数，表示以POST方式发送请求
'''
'''
1、发送GET请求
'''
# #以GET方式访问百度首页，返回的是百度首页的网页源代码
# response=urllib.request.urlopen("http://www.baidu.com")
# #response.read()获取网页内容，需要使用utf8编码对内容转码才能正常显示
# print(response.read().decode("utf8"))

'''
2、发送POST请求
'''
#以POST方式访问”http://httpbin.org/post“网站

# #与HTTP请求一起发送的数据
# param_dist={"key":"hello"}
# #调用urlencode函数将字典类型数据转成字符串
# param_str=urllib.parse.urlencode(param_dist)
# #将传输的数据封装成一个bytes对象
# param_datas=bytes(param_str,encoding='utf8')
# #在urlopen函数中传入data参数值，表示将发送一个POST请求
# response=urllib.request.urlopen("http://httpbin.org/post",data=param_datas)
# #打印网站返回的响应内容
# print(response.read())



#与HTTP请求一起发送的数据
#将传输的数据封装成一个bytes对象
param_datas=bytes("hello",encoding='utf8')
#在urlopen函数中传入data参数值，表示将发送一个POST请求
response=urllib.request.urlopen("http://httpbin.org/post",data=param_datas)
#打印网站返回的响应内容
print(response.read())

'''
3、超时时间
   通过设置timeout参数值避免由于请求超时造成程序崩溃
'''
# #设置请求超时时间
# #设置timeout参数值是0.001秒
# response=urllib.request.urlopen("http://www.baidu.com",timeout=0.001)
# print(response.read().decode("utf8"))

'''
4、响应状态码与头信息
'''
# #获取响应状态码
# response=urllib.request.urlopen("http://www.baidu.com")
# print(response.status)
#
# #获取响应头信息
# print("headers",response.getheaders())
# #获取头信息中的日期
# print("headers data:",response.getheader("Date"))
