# #定义函数，实现打印个人信息功能
# print("------无参函数：")
# def print_user_info():
#     print("姓名：小明")
#     print("年龄：20")
#     print("性别：男")
# #函数调用
# print_user_info()
#
# print("------有参函数：")
# def print_user_info2(name,age,gender):
#     print("姓名:",name)
#     print("年龄：{}".format(age))
#     print("性别：%s" %gender)
#
# name="小黑"
# age=25
# gender="男"
# print_user_info2(name,age,gender)
#
# print("\n-------缺省参数：")
# def x_y_sum(x,y=20):
#     rs=x+y
#     print(x)
#     print(y)
#     print("{}+{}={}".format(x,y,rs))
# #函数调用
# #只传入一个参数x的值
# x_y_sum(1)
# print("-----------")
# #传入缺省参数y的实参30
# x_y_sum(2,3)
#
#
# print("-------命名参数：")
# def x_y_sum2(x,y):
#     rs=x+y
#     print("{}+{}={}".format(x,y,rs))
# #注意：使用命名参数的参数名称必须与函数定义时的参数名称一致
# x_y_sum2(x=10,y=20)
# #不按照函数定义的形参顺序，通过指定参数名称传入实参
# x_y_sum2(y=30,x=15)
#
# print("------带有一个*的不定长参数(元组)：")
# print("计算任意多个数字的和：")
# def any_num_sum(*args):
#     print("args参数值：",args)
#     print("args参数类型：",type(args))
#     rs=0
#     #判断元组是否不为空
#     if len(args)>0:
#         #循环遍历元组，累加所有元素的值
#         for arg in args:
#             rs+=arg
#         print("总和：{}".format(rs))
#         print("__________")
# any_num_sum(1,2,3)
# any_num_sum(1,2)
# any_num_sum(1)
# any_num_sum()
#
# print("\n\n------带有两个*的不定长参数（字典）：")
# print("工资计算器：")
# def pay(basic,**kvargs):
#     print("kvargs参数值：",kvargs)
#     print("kvargs参数类型：",type(kvargs))
#     #扣除个人税金额
#     tax=kvargs.get('tax')
#     #扣除社保费用
#     social=kvargs.get('social')
#     #实发工资=基本工资-缴纳个税金额-缴纳社保费用
#     pay=basic-tax-social
#     print("实发工资：{}".format(pay))
#
# pay(8000,tax=500,social=1500)
#
#
#
# print("\n\n------拆包：")
# print("计算任意多个数字的和：")
# def any_num_sum(*args):
#     print("args参数值：",args)
#     print("args参数类型：",type(args))
#     rs=0
#     #判断元组是否不为空
#     if len(args)>0:
#         #循环遍历元组，累加所有元素的值
#         for arg in args:
#             rs+=arg
#         print("总和：{}".format(rs))
#         print("__________")
# #求数字列表中所有元素的累加和
# #数字列表
# num_list=[1,2,3,4]
# any_num_sum(*num_list)
#
#
#
# print("工资计算器：")
# def pay(basic,**kvargs):
#     print("kvargs参数值：",kvargs)
#     print("kvargs参数类型：",type(kvargs))
#     #扣除个人税金额
#     tax=kvargs.get('tax')
#     #扣除社保费用
#     social=kvargs.get('social')
#     #实发工资=基本工资-缴纳个税金额-缴纳社保费用
#     pay=basic-tax-social
#     print("实发工资：{}".format(pay))
#
# fee_dict={"tax":500,"social":1500}
# pay(8000,**fee_dict)
#
'''
#计算社保缴费金额
def insurance(basic,**kwargs):
    #医疗保险缴费比例
    health=kwargs.get("health")
    #养老保险缴费比例
    pension=kwargs.get("pension")
    #社保缴费金额=医疗保险缴费金额（缴费基数*缴费比例）+养老保险缴费金额（缴费基数*缴费比例）
    cost=basic*health+basic*pension
    #返回社保缴费金额
    return cost

#计算缴纳工资个税金额
def tax(balance):
    #根据余额选择属于哪个缴税区间，按照对应的缴税比例缴税
    if balance<=5000:
        #剩余工资小于等于5000不需要缴费
        return 0
    elif balance>5000 and  balance<=10000:
        #剩余工资大于5000并且小于10000税率为5%
        return balance*0.05
    elif balance>10000 and balance<=30000:
        # 剩余工资大于5000并且小于10000税率为10%
        return balance * 0.1
    else:
        #剩余工资30000以上税率20%
        return balance*0.2

#计算实发工资
def pay(basic):

    #社保中医疗保险和养老保险的缴费比例
    cost_dict={"health":0.02,"pension":0.08}

    #计算社保缴费金额
    cost=insurance(basic,**cost_dict)

    #工资余额=缴费基数-社保花费
    balance=basic-cost

    #计算个税缴费金额
    tax_fee=tax(balance)

    #实发工资=基本工资 - 社保费用 - 个税
    pay_fee=basic-cost-tax_fee
    print("基本工资：{},社保缴费：{}，个税：{}，实发工资：{}".format(basic,cost,tax_fee,pay_fee))

#程序执行入口
pay(8000)
'''
'''
def print_info1():
    #局部变量
    name="小明"
    age="20"
    print("name:{},age:{}".format(name,age))
def print_info2():
    #与print_info1函数中局部变量同名的局部变量
    name="小黑"
    age="25"
    print("name:{},age:{}".format(name,age))
print_info1()
print_info2()


#全局变量
g_value=1000
def sum(x):
    #使用global关键字声明全局变量
    global g_value
    g_value=5  #在函数内修改全局变量的值会使全局变量的值被完全更改
    rs=g_value+x
    print("{}+{}={}".format(g_value,x,rs))
#乘积
def product(x):
    rs=g_value*x
    print("{}*{}={}".format(g_value,x,rs))
#函数调用
print(g_value)
sum(20)
print(g_value)
product(20)


#使用递归函数计算3的阶乘
def factorial_func(num):
    if num>1:
        return num*factorial_func(num-1)
    else:#结束递归的判断，当num=1时，已经递归到了最后一步，直接返回1
        return num
#计算3 的阶乘
print(factorial_func(3))


print("1、将匿名函数赋值给变量，通过变量名调用匿名函数:")
sum=lambda x,y:x+y
print(sum(1,2))

print("2、匿名函数作为普通函数的参数：")
def x_y_compute(x,y,func):#func是匿名函数
    print("x={}".format(x))
    print("y={}".format(y))
    result=func(x,y) #将x和y两个参数使用func匿名函数进行计算
    print("result={}".format(result))

#传入的匿名函数用于求两个数的和
func1=lambda x,y:x+y
x_y_compute(1,2,func1)
#传入的匿名函数用于求两个数的乘积
func2=lambda x,y:x*y
x_y_compute(1,2,func2)


#普通函数求两个数字的和
def sum(x,y):
    return x+y

#闭包求两个数字的和
#外部函数
def sum_closure(x):
    #内部函数
    def sum_inner(y):
        #调用外部函数的变量x
        print("x:{},y:{}".format(x, y))
        return x+y
    #外部函数的返回值是内部函数的引用

    return sum_inner
rsl=sum(10,1)
print("普通函数：")
print("rsl:{}".format(rsl))
print("rsl的类型：",type(rsl))
print("---------")

rs_func=sum_closure(10)
print("rs_func:{}".format(rs_func))
print("rs_func的类型：",type(rs_func))

rs2=rs_func(1)
print("rs2:{}".format(rs2))
print("rs2的类型：",type(rs2))

'''

print("使用普通函数实现计数器：")
'''
参数说明：
   base：整型，表示基准值，计数器在基准值上累加，初始值为0
   step：整型，表示步长，初始值为1
'''

def counter_func(base=0,step=1):
    return base+step
c1=counter_func()
print("当前计数器的值为：{}".format(c1))
c2=counter_func(c1)
print("当前计数器的值为：{}".format(c2))
c3=counter_func(c2)
print("当前计数器的值为：{}".format(c3))

print("\n\n使用闭包实现计数器：")
def counter_closure(base=0):
    #在外部函数中定义一个列表类型的变量，存储计数器的累加基数
    cnt_base=[base]
    def counter(step=1):
        cnt_base[0]+=step
        return cnt_base[0]
    return counter
counter=counter_closure()
print("当前计数器的值为：{}".format(counter()))
print("当前计数器的值为：{}".format(counter()))
print("当前计数器的值为：{}".format(counter()))