
# 函数
## 函数是功能和动作集合的封装



## 定义函数
def fun():
    print("hello world")
    print("hello world")
    print("hello world")
    print("hello world")
    print("hello world")


## 调用函数
fun()



## 函数返回值
## return
def fun1():
    print("func1")
    return "hello"

### 没返回值,返回什么? --> 返回None
### 写了return,不给返回值 --> 也是返回None

### 多返回值--> 返回元组
print()
print("多返回值")
def func2():
    return "a","b","c"

ret = func2()
print(ret,type(ret))


## 函数参数
### 1.位置参数:即按形参的默认顺序进行传参
def func3(a,b,c):
    return 

func3(1,2,3)    ## 位置参数

### 2. 关键字参数:即按形参名进行赋值
func3(b=2,c=3,a=1)  ## 关键字参数

### 3. 混合参数:关键字和位置一起使用,要注意,位置参数的位置要正确(最好将位置参数放最左边)
func3(1,c=3,b=2)    ## 混合参数

## 缺省参数:和C++一样
### 缺省参数是可变数据类型时(如列表),坑:每次调用都会共享这个缺省参数(python不会析构,会一直重复使用)

## 动态参数
### 类似可变参数列表,自动将多个不定参打包成元组
print()
print("## 动态参数")

### 动态位置参数*
print()
print("## 动态位置参数")
def dynamic_local_func(*arg):
    print(arg,":",type(arg))

dynamic_local_func(1,2,3,"hello")

### 动态接收关键字参数
#### 动态关键字参数是一个字典
print()
print("## 动态关键字参数")
def dynamic_key_func(**arg):
    print(arg,":",type(arg))

dynamic_key_func(english="英语",chinese="中文")


### 混合参数正确顺序: 位置参数 > *args > 默认值参数 > **kwargs
#### 动态关键字+位置参数
print()
print("## 动态关键字+位置参数")
def dynamic_key_func1(a,**arg): ## 和缺省参数同理,要放在动态关键字参数前面
    print(a,arg,":",type(arg))  

dynamic_key_func1(1,english="英语",chinese="中文")


## 数据结构打散传参操作
def fun(*args):
    return

## 动态位置参数
lst = ["zhangsan","lisi","wangwu"]
fun(*lst)   ## 等效于: fun("zhangsan","list","wangwu")

## 动态关键字参数同理
def fun(**args):
    return

dic = {"name":"zhangsan","age":18}
fun(**dic)


## 作用域
print()
print("## 作用域")
print(globals())    ## 打印全局作用域中的内容
print(locals())     ## 打印当前作用域中的内容

## 名称空间
## 名称空间分为:全局名称空间(全局域),内置名称空间(Python自带,也属于全局名称空间),局部名称空间(函数等局部作用域)

## 声明
### global:声明全局变量
a = 10
def fun():
    global a    ## 引入全局变量
    a = a+1
    print(a)

fun()

### nonlocal : 声明非局部变量(非全局变量,又非当前作用域变量,即介于全局与当前作用域之间的中间作用域,多层嵌套情况下使用)


