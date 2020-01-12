#引入模块，通过包名.模块名的方式引入
# import buss.model1
# import tool.model1

#引入不同包下的同名模块
'''
第一种方法：from 最外层包。子包。。。模块 import 该模块中的某一函数

from chapter05.buss.model1 import project_info
from chapter05.tool.model1 import tool_info

#分别调用两个同名模块中的不同函数
project_info()
tool_info()
'''

'''
第二种方法： 1.先从最外层包中import 两个包
            2.再分别从这两个包中import同名模块
from chapter05 import buss,tool
from chapter05.buss import model1
from chapter05.tool import model1

buss.model1.project_info()
tool.model1.tool_info()
'''

'''
第三种方法：

返回上一级目录查找
import sys
sys.path.append ("..")


'''

# from chapter05.buss.model1 import project_info
# from chapter05.tool.model1 import tool_info
#
# #分别调用两个同名模块中的不同函数
# tool_info()
# project_info()
'''
import sys
sys.path.append ("..")
import test_model
#from chapter05.test_model import test_info
def info():
    print("当前正在运行，__name__值={}".format(__name__))

print("---------")
info()
test_model.test_info()
'''
#返回到chapter05目录
import sys
sys.path.append("..")

import test_model #此句等价于把test_model中的所有代码粘贴到此位置
print('孔')
def info():
    print("当前正在运行，__name__值={}".format(__name__))

print("---------")
info()
test_model.test_info() #显示调用