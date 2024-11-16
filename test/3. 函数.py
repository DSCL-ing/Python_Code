
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
def dynamic_func(*arg):
    print(arg,":",type(arg))

dynamic_func(1,2,3,"hello")

### 动态接收关键字参数
