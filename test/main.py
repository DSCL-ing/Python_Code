
###### 一.第一个python程序
print("hello world")



###### 二.注释
# 这是注释吗

'''
这是注释吗
'''

"""这是注释吗"""

###### 三.类型
##### 1.整型 int类型

a = 3;
b = 4;

# 基本运算
print(a+b)
print(a-b)
print(a*b)
print(a/b)  # 小数点除
print(a//b) # 整除,地板取整
print(a%b)

# 比较
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

# "+" 与 "*"
print(s+s1)   ## 字符串拼接
# print(s+1)  """ 字符串只能和字符串拼接 """
print(s*5)    ## 字符串重复,只能*整数

##### 3.布尔类型 bool类型
# true/false

# flag = false

###### 查看变量类型
# type(变量)
print(type(a))
print(type(s))
print(type(a<b))


