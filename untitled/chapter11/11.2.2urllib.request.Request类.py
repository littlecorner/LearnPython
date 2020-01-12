#在Request对象中添加浏览器相关的头信息，把程序伪装成浏览器发送POST请求

#引入parse模块
import urllib.parse
import urllib.response
import urllib.request

url = "http://httpbin.org/post"
#设置浏览器信息
headers={"User-Agent":"Mozilla/5.0(Macintosh;Intel Mac OS X 10_13_6) AppleWebKit/537.36(KHTML,like Gecko)Chrome/69.0.3497.100 Safari/537.36"}
data_dict={"word":"hello world"}
#将字典类型数据转换成bytes字节流
data=bytes(urllib.parse.urlencode(data_dict),encoding='utf8')

#创建Request对象
request_obj=urllib.request.Request(url=url,data=data,headers=headers,method="POST")
response=urllib.request.urlopen(request_obj)
print(response.read().decode("utf8"))
