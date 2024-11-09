
###### 一.第一个python程序
print("hello world")



###### 二.注释
# 这是注释吗

'''
这是注释吗
'''

"""这是注释吗"""

###### 三.变量类型
print("###### 三.变量与类型")
print("## 整型")
# 1.整型 int类型
a = 3
b = 4
## 字符串转int
print()
print("字符串转整型")
print(int("123"))


# 基本运算
print()
print('###### 基本运算')
print(a+b)
print(a-b)
print(a*b)
print(a/b)  # 小数点除
print(a//b) # 整除,地板取整
print(a%b)
print(a**b) # **表示次幂,a为底数,b为幂数,即a的b次幂


# 逻辑运算
print()
print('# 逻辑运算')
print(True and False)
print(True or False)
print(True or True and False or not True)
## 优先级: () -> not -> and -> or
## 同义: 零为假,非零为真

# 比较
print()
print("# 比较")
print(a<b)
print(a==b)

##### 2.字符串 str类型
s = 'abc'
s1 = "def"
s2 = '''ghi 
'''
print(s)
print(s1)
print(s2)

## 字符串的"+" 与 "*"运算
print()
print("## 字符串的\"+\" 与 \"*\"运算 ")
print(s+s1)   ## 字符串拼接
# print(s+1)  """ 字符串只能和字符串拼接 """
print(s*5)    ## 字符串重复,只能*整数

## str(变量): 转字符串 
print()
print("## str(变量): 转字符串 ")
print(str(True))
print(str(123))
print(str([1,2,3]))
    
## 字符串的索引(下标)
print()
print("## 字符串(字符数组)的索引")
'''
与C/C++等区别是, python下标负数就是倒过来索引
'''
s = '我是你爹'
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[-1])
print(s[-2])
print(s[-3])
print(s[-4])

##### 3.布尔类型 bool类型
print()
print("##### 3. 布尔类型")

# True/False
flag = False

# bool(变量) : 将数值转化成bool值

## bool(字符串)
print(bool(""))          # 只有空串是false
print(bool(" "))
print(bool("任意字符"))  # 其他都是true

## bool(list) # list: 列表类型
a = []                  # 空列表是False
print(bool(a))
a = [1,2,3,4]           # 其他都是True
print(bool(a))
    
## 所有空的东西都可以表示False

###### 4.查看变量类型
print()
print("打印变量类型")
# type(变量)
a = 1
s = ""
b = 2
flag = False
print(type(a))      # <class 'int'>
print(type(s))      # <class 'str'>
print(type(a<b))    # <class 'bool'>
print(type(flag))   # <class 'bool'>




    
###### 5. 输入
# name = input("请输入的你名字:")
"""
    input接收的所有数据都是字符串
"""

##### 6. 将字符串转化成数字
# a = input("a:")
# b = input("b:")
# print("a+b=",int(a)+int(b))

# print("a+b=",int(input("a:"))+int(input("b:")))

###### 7.常量
""" 
python中所有大写字母约定为常量,不可改变
"""

###### 8. bytes 类型
##  encode() : 编码

s = '中国'
print(s.encode('utf-8')) # b'\xe4\xb8\xad\xe5\x9b\xbd'  # 每个汉字占3字节
print(s.encode("GBK"))   # b'\xd6\xd0\xb9\xfa'          # 每个汉字占2字节

## decode() : 解码
print(s.encode('utf-8').decode("utf-8"))                # 中国
print(s.encode('GBK').decode("gbk"))                    # 中国



###### 四. 条件
"""
if的代码块以table符为界
python的代码块都是以table为界
"""

# money  = int(input())
# 
# if money>1000:
#     print("a")
#     print("aa")
# elif money>500:
#     print("b")
# else:
#     if money>50:
#         print("50-500")
#     else:
#         print("<=50")
#     print("c")
# print("d")


###### 五. pass:python中占位语法,什么都不做.起到填充语法结构的作用

###### 六. while - break - continue 

# while True:
#     if input()=="1":
#         continue
#     else:
#         break


###### 七. 字符串格式化输出

# 按照以下格式输出字符串
'''
name: zhangsan
age: 18
job: 开车
hobby: 吃饭
'''


name = input("姓名:");
age = input("年龄:");
job = input("工作:");
hobby = input("爱好:");

##### 1. 原始方案
# s = '''
# name: %s
# age: %s 
# job: %s
# hobby: %s
# ''' %(name,age,job,hobby);
# print(s);

##### 2. python3.5以后支持的新方案
ss = f'''
name: {name}
age: {age}
job: {job}
hobby: {hobby}
''' 
print(ss)






