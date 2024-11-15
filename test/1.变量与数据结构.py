
###### 一.第一个python程序
print("hello world")



###### 二.注释
# 这是注释吗

'''
这是注释吗
'''

"""这是注释吗"""

###### 三.变量
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
print()
print("##### 2.字符串 str类型")
s = 'abc'
s1 = "def"
s2 = '''ghi 
'''
print(s)
print(s1)
print(s2)

## 字符串的"+" 与 "*"运算
print("## 字符串的\"+\" 与 \"*\"运算 ")
print(s+s1)   ## 字符串拼接
# print(s+1)  """ 字符串只能和字符串拼接 """
print(s*5)    ## 字符串重复,只能*整数

## str(变量): 转字符串 
print("## str(变量): 转字符串 ")
print(str(True))
print(str(123))
print(str([1,2,3]))
    
## 字符串的索引(下标)
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
    
#### 字符串的相关操作
### 字符串是不可变对象,任何字符串操作都对原字符串不造成影响
## 字符串切片
print("## 字符串切片")
print(s[1:2]) ## 前闭后开
print(s[1:])  ## 1开始全部切(包含1)
print(s[:3])  ## 切到3(不包含3)
print(s[3:1]) ## 无效:默认情况是从左往右切
### 上述情况是以默认步长1进行移动
### 切片函数原型为: s[左:右:步长] 其中,步长不能为0
s = "abcdefgh"
print(s[1:5:2]) ## 含义在bcde中,每两步切一个:即bd
print(s[0:8:3]) ## abcdefgh中,每3步切一个:  即adg
print(s[3:0:-1])   ## 反向,从dcb中反向每一步都切,即dcb
print(s[3::-1]) 

## 字符串首字母大写
print("## 字符串首字母大写")
s = 'i am superman'
print(s.capitalize())

## 字符串全变成小写  --# lower识别不够全,没有upper强大(python共识使用upper来忽略大小写)
print("## 字符串全变小写")
s = 'i am superman'
print(s.lower())
print(s.casefold()) ## 也是全变小写,但功能比lower更强大,能够识别更多
    
## 字符串全大写
print("## 字符串全大写")
s = 'i am superman'
print(s.upper())
    
## 字符串大小写互转
print("## 大小写互转")
s = 'I Am MonkeyKing!'
print(s.swapcase())
    
## 句子/段落中的所有单词的首字母大写(英语标题)
s = "i am super_monkey!"
print(s.title())

## 字符串居中 
# center(格式化宽度,填充字符=" ")
print()
print("## 字符串居中")
s = "exit"
print(s.center(10))
print(s.center(10,"*"))

## 去掉字符串左右空白("空格","\t","\n"),俗称"脱衣",方便用户去掉多余的空格换行等
print()
print("## 去掉字符串左右空白")
s = " \n  i am super_monkey!   \t "
print(s.strip())
# 指定去掉两边的内容
s = "a_kkk_a"
print(s.strip("a")) ## 输出: _kkk_

## 字符串替换
print()
print("## 字符串替换")
s = '我是超人'
print(s.replace("超人","***"))
# 去掉字符串中所有的空格
print("# 去掉字符串中所有的空格")
s = "a b c d e f g"
print(s.replace(" ",""))

## 字符串切割
s = "zhangsan_lisi_wangwu_zhaoliu"
l = s.split("_")   ## list类型
print(l)    # ['zhangsan', 'lisi', 'wangwu', 'zhaoliu']


## 列表组合成字符串
print()
print("## 列表组合成字符串")
print("_".join(l)) # zhangsan_lisi_wangwu_zhaoliu 



##  字符串格式化输出
print()
print("##  字符串格式化输出")
# 按照以下格式输出字符串
'''
name: zhangsan
age: 18
job: 开车
hobby: 吃饭
'''

## 假设以下数据是input的
name = 'zhangsan'
age = "18"
job = '开车'
hobby = "吃饭"

## 1. 原始方案
print("## 1. 原始方案")
s = '''
name: %s
age: %s 
job: %s
hobby: %s
''' %(name,age,job,hobby);
print(s);

## 2. python3.5以后支持的新方案
print("## 2. python3.5以后支持的新方案")
ss = f'''
name: {name}
age: {age}
job: {job}
hobby: {hobby}
''' 
print(ss)

## 3. format()方式1,默认顺序
print("## 3. format()方式1")
ss = '''
name: {}
age: {}
job: {}
hobby: {}
'''.format(name,age,job,hobby)
print(ss)

## 4. format() 方式2,自定义顺序
print("## 4. format()方式2")
ss = '''
name: {3}
age: {2}
job: {1}
hobby: {0}
'''.format(hobby,job,age,name)
print(ss)

## 4. format 方式3, 别名
print("## 5. format()方式3")
ss = '''
name: {n1}
age: {n2}
job: {n3}
hobby: {n4}
'''.format(n1 = name,n2=age,n3=job,n4=hobby)
print(ss)


# 判断字符串是否以特定字符串开头
print()
print("# 判断字符串是否以特定字符开头")
s = "zhangsan"
print("start is zhang?")
if s.startswith("zhang"):
    print(True)
else:
    print(False)

## 判断字符串是否以特定字符串结尾
print("end is san?")
if s.endswith("san"):
    print(True)
else:
    print(False)

# 统计字符串中特定字串出现的次数
print()
print("# 统计字符串中特定字串出现的次数")
s = "hello world!"
print(s,"中出现o的次数:",s.count("o"))

# 查找字串出现的位置
print()
print("# 查找字串出现的位置")
s = "hello world!"
print(s,"中第一个字母r出现的下标:",s.find("r"))
print(s,"中第一个字母s出现的下标:",s.find("s"))     ## 找不到则返回-1
## index与find功能一致,唯一区别是,index找不到时会报错
# print(s,"中第一个字母s出现的下标:",s.index("s"))     ## 找不到则报错

# 判断字符串是否由数字组成
print()
print("# 判断字符串是否由数字组成")
s = "abc123"
if s.isdigit():
    print("是数字,可以计算")
    print(int(s))
else:
    print("不是纯数字,输入有误")
    
## 判断字符串是否是小数
s.isdecimal()

## 判断字符串是否是"数字"(大写小写阿拉伯等常见数字写法都能识别)
s.isnumeric()

# 查看关键字源代码包含的方法
str  ## 输入关键字,然后访问源代码

#  打印关键字能够执行的操作/函数
## print(dir(关键字))
print(dir(str))



## python中直接就能用的函数叫内置函数
print()
print("###### 内置函数")
# 计算字符串长度 len()
print("# 计算字符串长度")
s = "123"
print(len(s))



# 迭代器for循环
## for 变量 in 可迭代对象
print()
print("# 迭代器for循环")
s = "abcdefg"
for c in s:
    print(c)

# in
## in有两种用法
## 1. 在for循环中表示属于可迭代对象
## 2. 不在for中,用于判断字串是否在str中
print("## 2. 不在for中的in,用于判断字串是否在str中")
print("a" in "abcdef")










###### 布尔类型 bool类型
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

## while - else
print()
print("## while-else")
i = 10
while i<10:
    print(i)
    i-=1
else:
    print("OK!")    ##循环条件不满足时,就会执行else; 注意,else的条件是while条件运算返回False值
    
i = 10
while i<10:
    print(i)
    if i == 7:
        break   ## 如果是break,则不会执行else; 因为break是跳出循环,并不执行最后的while条件判断
else:
    print("OK!")

### <-----break跳出的位置


###### 七. 内置函数


###### list类型(列表)
print()
print("###### list类型(列表)")
# 列表的索引
print("# 列表的索引")
lst = ["zhangsan","lisi","wangwu","zhaoliu"]
print(lst[3])   ## zhaoliu

# 列表的切片
## 列表切片的结果还是列表
print()
print("# 列表的切片")
lst = ["zhangsan","lisi","wangwu","zhaoliu"]
print(lst[::1]) ## ['zhangsan', 'lisi', 'wangwu', 'zhaoliu']    jk

# 列表的追加
print()
print("# 列表的追加")
lst = ["zhangsan"]
lst.append("lisi")  ##['zhangsan', 'lisi']
print(lst)

# 列表的插入
## insert(下标,元素),将元素插入到指定下标后面
print()
print("# 列表的插入")
lst = ["zhangsan","wangwu"]
lst.insert(1,"lisi")
print(lst)      ## ['zhangsan', 'lisi', 'wangwu']


# 列表的迭代新增
print()
print("# 列表的迭代新增")
n = ["aaa","bbb",123,True]  ## list支持不同类型
lst.extend(n)
print(lst)      ## ['zhangsan', 'lisi', 'wangwu', 'aaa', 'bbb']

# 列表的删除
print()
## remove("元素"),  删除指定元素
print("## remove(\"元素\"),  删除指定元素")
lst = ["zhangsan","lisi","wangwu","zhaoliu"]
lst.remove("lisi")
print(lst)      ## ['zhangsan', 'wangwu', 'zhaoliu']


## pop(下标=-1) , 删除特定下标的元素,缺省值是-1,即最后一个元素
## pop(), 删除末尾元素(像一个栈,后进先出)
print()
print("## pop()")
lst = ["zhangsan","lisi","wangwu","zhaoliu"]
ret = lst.pop()     ## 具备top()的功能,一步到位删除+获取返回值
print(lst)   ## ['zhangsan', 'lisi', 'wangwu']

print()
print("## pop(下标) , 删除特定下标的元素")
lst = ["zhangsan","lisi","wangwu","zhaoliu"]
lst.pop(1)
print(lst)   ## ['zhangsan', 'wangwu', 'zhaoliu']


# 清空列表
print()
print("# 清空列表")
lst = ["zhangsan","lisi","wangwu","zhaoliu"]
lst.clear()
print(lst)

# 列表的方括号[]
## []:和数组一样
print()
print("# 列表的方括号[] ")
lst = ["zhangsan","lisi","wangwu","zhaoliu"]
lst[1] = "lisiiiiiiii"
print(lst)

## 列表的逆置 reverse
print()
print("## 列表的逆置 reverse")
lst = ["zhangsan","lisi","wangwu","zhaoliu"]
lst.reverse()
for i in range(len(lst)):
    print(lst[i])

## 列表排序
print()
print("## 列表排序")
lst = [2,5,1,7,4]
lst.sort()              ## 默认升序
print(lst)
lst.sort(reverse=True)  ## 逆序
print(lst)

## range
### range()用于表示一段范围,
### range(n)    
print()
print("## range")
for i in range(len(lst)):
    print(lst[i])
    print(i)


### range(m,n)
print()
for i in range(5,10):
    print(i)

### range(m,n,s)
print()
for i in range(1,10,2):
    print(i)
    
### 找人
print()
print("### 找人")
lst = ["zhangsan","lisi","wangwu","zhaoliu"]
for i in range(len(lst)):
    item = lst[i]
    if item.startswith("wang"):
        print(i)
        



## 元组tuple
### 元组:只读列表,只能看
### 与列表类似,列表是中括号,元组是小括号
print()
print("## 元组tuple:只读列表")
### Exam
print("### Exam")
t = ("a","e","g")
print(t)
print("### 类型")
print(type(t))
print("### 切片")
print(t[:2])
# t[1] = 'b'        ## error:不支持修改

### 元组的坑
print()
print("### 元组的坑: 一个元素的元组")
### 1个元素的元组"不是元组"
t = ("a")       ## 实际是括号的优先级用法
print(t)
t = (1)
print(t)        ## 实际是括号的优先级用法

### 正确用法
print()
print("### 一个元素的元组的正确写法")
t = (1,)
print(t)        ## (1,)


### 元组元素值不可变,但元素指向的对象可变
print()
print("### 元组元素值不可变,但元素指向的对象可变")
t = ("abc",123,[])
print(t)
t[2].append("hello")
print(t)

### 解构
print()
print("解构")
a = 1,2
print(a)    ## a是一个元组(1, 2)
a,b = 1,2   ## 将元组(1,2)解构后分别赋给变量a和b
a,b = (1,2) ## 将元组(1,2)解构后分别赋给变量a和b





## 字典dict
print()
print("## 字典")
### 类似C++中的map,存储键值对的数据结构
### key的要求:字面值的数据类型: int,str,tuple,bool; 不可哈希的类型list,dict,set
### 语法: {key1:value, key2:value, ...}

d = {"apple":"苹果","banana":"香蕉","oringe":"橙子"}
print(d)
print(d["apple"])

### 新增和修改都是[]
print()
print("## 新增")
ret = d.setdefault("english","错误")    ## 新增+返回,但不能修改
print(d)
print(ret)
d["english"] = "英语"   ## 没有则新增,有则修改
print(d)
ret = d.setdefault("english","正确")    ## 无效:{'apple': '苹果', 'banana': '香蕉', 'oringe': '橙子', 'english': '英语'}
print(d)


### 删除
print()
print("### 删除")
ret = d.pop("english")
print(ret)
d.clear()   ## 全删
print(d)


### 查询
print()
print("## 查询")
d = {"apple":"苹果","banana":"香蕉","oringe":"橙子"}
print(d["apple"])       ## key不存在报错
print(d.get("apple"))   ## key不存在返回空
print(d.get("不存在","默认值"))     ## key不存在时,还可以返回默认值


### 遍历
print()
print("### 字典的遍历")
d = {"apple":"苹果","banana":"香蕉","oringe":"橙子"}
print(1)
for k in d:     ## 方式1:for遍历返回的是值是key
    print(k)    ## key
    print(d[k]) ## 获取value的方式
    print(d.get(k)) ##或者
    
print()
print("### 2. dict.keys()")
print(d.keys())         ## dict_keys(['apple', 'banana', 'oringe'])
print(type(d.keys()))   ## keys()返回的是dict_keys的类型:<class 'dict_keys'>
for k in d.keys():
    print(d[k])
    
print()
print("### 3. dict.values()")
for val in d.values():      ## 直接获取value
    print(val)
    
print()
print("### 4.dict.items()") ## 返回字典的每一项<key-value>元组
print(d.items())
for item in d.items():
    print(item)
    k,v = item      ## 解构
    print(k,v)


## set
### 集合:
### 特点:1.去重 2.无序(不能使用索引)
print()
print("### 集合")

### 交并差
s1 = {"a","b","c"}
s2 = {"b","c","d"}
#### 求s1与s2交集
print()
print(s1)
print(s2)
print("交集:",s1&s2)

#### s1与s2并集
print()
print("并集",s1|s2)

#### s1与s2差集
print()
print("差集",s1-s2)


### 创建set集合
print()
print("创建set集合")
s = set()
print(type(s))
print("创建dict字典")
# d = {}    ## 默认是字典
d = dict()
print(type(d))

### set删除:先删再加
print()
print("set删除")
s = {
    'a','b','c'
}
print("s:",s)
s.remove("a")
s.add("d")
print(s)

### 遍历
print()
print("遍历set")
for item in s:
    print(item)
    


## 地址/深浅拷贝
print()
print()
print("地址/深浅拷贝")
a = ["a","b","c"]
b = a       ## 浅拷贝
print(id(a))
print(id(b))

b = a.copy()    ## 假"深"拷贝
print(id(a))
print(id(b))

b = a[:]        ## 假"深"拷贝(切片也是生成一个新对象)
print(id(a))
print(id(b))

## 假"深"拷贝
a.append([1,2,3])
b = a.copy()
print(a)
print(b)
a[3].append(4)
print(a)
print(b)


print()
print("真.深拷贝")
import copy     ## 导入深拷贝模块
b = copy.deepcopy(a)        ## 真.深拷贝
a.pop()
print(a)
print(b)


## Python中数据结构的统一删除方式" ,例一
print()
print("## Python中数据结构的统一删除方式")
print("法一")
lst = ["zhangsan","zhanglao","zhangwu","lisi"]
i = len(lst)
j = 0
while(j<i):
    if lst[j].startswith("zhang"):
        lst.pop(j)
        i-=1
        j-=1    ## 让j保持不动
    j+=1
    
print(lst)
    
print()
print("法二")   ## 统一方式
## 问题:没有迭代器缺陷,无法弥补迭代器失效的问题
new_lst = list()
for item in lst:
    if item.startswith("zhang"):
        new_lst+=item
    
for item in new_lst:
    lst.remove(item)

print(lst)

print()
print("法三")   ## 统一方式
## 利用切片返回的拷贝对象的原理,对拷贝对象进行遍历(原对象删除后会导致遍历不到位,删除不完全;拷贝对象不删除只遍历,保证遍历到位)
for item in lst[:]: 
    lst.remove(item)    
    

## 删除,例二:字典
d = {"apple":"苹果","banana":"香蕉","english":"英语"}

## 错误示例:字典不允许在遍历过程中删除
# for item in d.keys():
#     d.pop(item) ## dictionary changed size during iteration

lst = list(d.keys())    ## 保证字典遍历过程中大小不会被改变
for item in lst:
    d.pop(item)
    



## "is" 和 "=="
print()
print(" is 和 ==")
a = [1,2,3]
b = [1,2,3]
print(a == b)   ## == 比较的是对象内容是否相等
print(a is b)   ## is 比较的是对象的地址是否相等

### 一般用is来判空(is用的不多,要么判空要么判地址)
print()
print("一般用is来判空")
c = None
if c is None:
    print("c 是 空")
else:
    print("c 不是空")



