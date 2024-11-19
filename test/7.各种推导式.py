

## 列表推导式(语法糖)
## 语法: lst = [1.结果(item的表达式) 2.for-item循环 3.for中的if条件]
print("## 列表推导式")



## 来由:
lst = []
for i in range(1,10):
    if(i%2==1):
        lst.append(i)
print(lst)
print()



## exam1
## 获得1-9的列表
lst = [i for i in range(1,10)]
print(lst)
print()

## exam2
## 获得1-9奇数
lst = [i for i in range(1,10) if i%2==1]
print(lst)
print()

## exam3
## 获得1-9,奇数的立方
lst = [i**3 for i in range(1,10) if i%2==1]
print(lst)
print()

## exam4
## 模拟弹幕
lst = ["yyds x %s"%i for i in range(1,10)]
print(lst)
print()


## 字典推导式
## 语法: dic = {1.key(i的表达式):value 2.for-i循环 3.for中if条件}
print("## 字典推导式")

### exam1:
### key为下标,value为列表元素值
lst = ["zhangsan","lisi","wangwu"]
dic = {i:lst[i] for i in range(len(lst)) }
print(dic)
print()


## 集合推导式
## 语法: s = {1.key(i的表达式) 2.for-i循环 3.for中的if条件}
print("## 集合推导式")
s = {item for item in lst}
print(s)
print()


##  生成器表达式
### 什么推导式都有了,好像就差元组推导式,看起来也像元组推导式,但注意因为元组是不可变类型(不能修改),因此python中并不存在元组推导式
l = (i for i in range(10))  
print(l)    ## 生成器推导式 <generator object <genexpr> at 0x00000241FFD86110>


## 取走生成器的数据
### 通过遍历
print()
print("## 取走生成器的数据1")
for i in l:
    print(i)    
## 走到这里时，生成器l已经走完了，之后就是空值

### 通过数据结构取走
print()
print("## 取走生成器的数据2")
l = (i for i in range(10))     ## 重新构造生成器
print(set(l))

# l = (i for i in range(10))     ## 重新构造生成器
# print(dict(l))                 ## 字典是键值对的哈希表，需要键值对

l = (i for i in range(10))     ## 重新构造生成器
print(tuple(l))

l = (i for i in range(10))     ## 重新构造生成器
print(list(l))


## 题目
print()
print("## 生成器用例题")
def func():
    print(111)
    yield 222

g = func()              ## 创建生成器
g1 = (i for i in g)     ## 创建生成器
g2 = (i for i in g1)    ## 创建生成器

print(list(g))          ## list取走g中数据
print(list(g1))         ## g1准备取走g中数据，但是g为空了，所以也为空
print(list(g2))         ## g2同g1