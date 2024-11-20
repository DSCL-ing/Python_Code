
## callable: 判断对象是否可调用

def func(fn):
    fn()    ## 如果fn不可被调用就会崩掉

def func(fn):
    if callable(fn):
        fn()
    else:
        print("is not callable")


## help(对象)   :打印说明文档,在命令行模式下中好用

## __import__(模块名) : 动态加载模块
### Usage: 
print()
name = "os"
__import__(name)


## eval: 
### 可以把字符串当代码执行
### exam1:能够计算字符串格式的数学表达式
print()
s = "1+1"
print(eval(s))
### exam2:
print()
s= "[1,2,3]"
print(eval(s))

## exec
print()
s = "a = 100"
exec(s)     ## 没有返回值
print(a)


## 进制
print()
### bin,oct,hex
a = 5
print(bin(a))   ## 0b101
print(oct(5))   ## 0o5
print(hex(5))   ## 0x5


## 数学运算
print()
### 绝对值 abs(数)

### 除法   divmod(被除数,除数) 结果:(商,余数)
print(divmod(10,3))     ## 结果:(3,1)   
#### 更常用的是// 和 %

### 四舍五入
print(round(4.56))  ## 5

### 次方 pow(底数,指数) ,等价于2**10
print(pow(2,10))
print(2**10)

### 求和 sum(可迭代对象) 
print(sum([1,2,3,4,5]))

### 最大值/最小值 max(可迭代对象)
print(max(1,2))
print(min(1,2,3))


## 数据结构
### 不可变集合 frozenset    (不可变列表就是元组)

### enumerate(数据结构,起始值=0) 返回元素的索引和值构成的元组:(索引,值)
lst = ["a","b","c"]
for item in enumerate(lst):
    print(item,end=" ") ## (0, 'a') (1, 'b') (2, 'c')
print()

for item in enumerate(lst,10):
    print(item,end=" ") ## (10, 'a') (11, 'b') (12, 'c')
print()


## any(可迭代对象)/all(可迭代对象) ## 将可迭代对象所有东西 or / and
print()
lst = [0 ,1 ,2]
print(any(lst))     ## or
print(all(lst))     ## and

## zip(可迭代对象1,可迭代对象2,...) ## 将可迭代对象竖式拉链到一起
print()
lst1 = [1,2,3]
lst2 = ['a','b','c']
print(dict(zip(lst1,lst2)))     ## {1: 'a', 2: 'b', 3: 'c'}


## reversed（列表) ,列表翻转
print()
lst = [1,2,3]
r = reversed(lst)
print(list(r))




## slice    切片 s[1:4:2] 的代码版，优点是能固定切片方案
ss = slice(1,4,2)
s1 = "123456789"
s2 = "abcdefghi"
print(s1[ss])
print(s2[ss])

## ord(c)/chr(c)    字符转字符代码/字符代码转字符
print(ord('中'))    ## 20013
print(chr(20013))   ## 中

### chr可以用来生成验证码 
import random
n = random.randint(65,93)
print(chr(n))


## repr：返回字符串的字符串原始字面值(转义字符也会原封不动输出),并且是标准字符串 --- 太抽象了
## r字符串: 返回字符串的字符串原始字面值(转义字符也会原封不动输出)


## format
a = 48
print(format(a,"08d"))  ## 00000048

b = 5
print(format(b,"b"))    ## 101
print(format(b,"08b"))  ## 00000101