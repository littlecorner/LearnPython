'''
1、URLError：
   通过reason属性可以获取产生URLError的原因
   产生URLError的两种原因：网络异常，失去网络连接
                          访问的服务器不存在，服务器连接失败
'''

#访问一个不存在的URL，捕获URLError异常
import urllib.response
import urllib.request
import urllib.parse
import urllib.error

# #一个不存在的链接
# url="http://www.hhhdddmmm123.com"
# try:
#     request_obj=urllib.request.Request(url=url)
#     response=urllib.request.urlopen(request_obj)
# except urllib.error.URLError as e:
#     print(e.reason)
'''
2、HTTPError：是URLError的子类，如果两个异常全部捕获，需要先捕获HTTPError，再捕获URLError，否则将无法捕获到HTTPError
   
'''
#访问一个不存在的URL，捕获HTTPError和URLError，并获取异常原因、响应状态码、请求头信息
try:
    response=urllib.request.urlopen("http://www.123456.com/abc")
except urllib.error.HTTPError as e:
    print("捕获HTTPError异常，异常原因：",e.reason)
    print("响应状态码：",e.code)
    print("请求头信息：", e.headers)
except urllib.error.URLError as err:
    print("捕获URLError异常，异常原因：",err.reason)