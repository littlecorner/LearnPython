'''
1、GET请求：
   通过requests内置的get函数可以发起一次GET请求，通常在get函数中传入两个参数
   第一个必选参数是：要访问的URL
   第二个可选参数是：一个命名参数params，该参数的值会被传输到目标站点服务器，并且将参数拼接到URL之后
   发送请求成功后，会返回一个requests.models.Response对象，通过Response对象内置的方法可以获取更多我们想要的信息
'''
import requests
# #向测试地址“http://httpbin.org/get”发送GET请求
# response=requests.get("http://httpbin.org/get")
# print("response类型：{}".format(type(response)))
# print("状态码status_code={}".format(response.status_code))
# #获取响应内容,返回的响应内容中args对应的值就是通过GET请求传输到服务端的参数
# print(response.text)

# #向测试地址“http://httpbin.org/get”发送GET请求,同时传输两个参数 key=python   page=10
# # response=requests.get("http://httpbin.org/get?key=python&page=10")
# # print("请求的url:{}".format(response.url))
# # print("响应的内容：{}".format(response.text))

# #改造后的代码:data字典中的键值对参数被自动添加到了请求的URL后面，整体代码逻辑非常清晰
# data={
#     "key":"python",
#     "page":10
# }
# response=requests.get("http://httpbin.org/get",params=data)
# print("请求的url:{}".format(response.url))

'''
2、POST请求
   通过requests内置的post函数可以发起一次POST请求，通常在post函数中传入两个参数
   第一个必选参数是：要访问的URL
   第二个可选参数是：一个命名参数data，该参数的值会被传输到目标站点服务器，但是不会像GET请求那样将参数拼接到URL之后，而是以form表单的形式提交到服务端
'''
#向测试地址“http://httpbin.org/post”发送POST请求,同时传输三个参数 key=python  version=3.6  page=10
# data={
#     "key":"python",
#     "version":3.6,
#     "page":10
# }
# response=requests.post("http://httpbin.org/post",data=data)
# print(response.text)

'''
3、添加headers头信息
  当使用程序模拟浏览器向服务器发送请求时，需要在请求中添加headers头信息。
'''
#编写爬虫程序，在京东商城搜索关键字“手机”，将搜索结果网页爬取下来
def spider_jd(keyword):
    #请求参数
    params={
        "keyword":keyword,
        "enc":"utf-8",
        "pvid":"c150090b2d79478fb921a5e6f4b067d8"
    }
    #请求头信息
    headers={
        #"User-Agent":"Mozilla/5.0(Macintosh;Intel Mac OS X 10_13_6)Apple WebKit/537.36(KHTML,like Gecko)Chrome/70.0.3538.110 Safari/537.36",
        "user-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36",
        "Referer":"https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&wq=%E6%89%8B%E6%9C%BA&pvid=66838f5f99f34236a8d8db491e3853e4",
        "host":"search.jd.com",
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Language":"zh-CN,zh;q=0.9"
    }
    url="https://search.jd.com/Search"
    #获取网页内容
    response=requests.get(url=url,headers=headers,params=params)
    #通过状态码判断是否获取成功
    if response.status_code==200:
        #回去响应内容编码格式
        print("encoding:{}".format(response.encoding))
        #为解决中文乱码问题，重新设置编码格式utf-8
        response.encoding='utf-8'
        print(response.text)
if __name__=='__main__':
    spider_jd("手机")

