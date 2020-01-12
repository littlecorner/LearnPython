'''
1、dumps函数:将用户信息字典转换成JSON编码的字符串
'''
import json
user_info_dict={"name":"zhangsan",
                "age":20,
                "language":["python","hadoop"],
                "study":{"AI":"python","bigdata":"hadoop"},
                "if_vip":True,
                "gender":None}
json_str=json.dumps(user_info_dict)
print("JSON编码：",json_str)

'''
2、loads函数：将JSON编码的字符串转换成Python数据结构
'''

python_dict=json.loads(json_str)
print("python编码：",python_dict)
#转换之后的类型
print("转换之后的类型：",type(python_dict))

'''
3、dump函数：将python数据写入到JSON文件
'''
with open("./user_info.json","w") as f:
    json.dump(user_info_dict,f)

'''
4、load函数：将JSON文件中的数据转化成python数据结构
'''
with open("./user_info.json","r") as f:
    user_info_dict=json.load(f)
    print("python编码：",user_info_dict)