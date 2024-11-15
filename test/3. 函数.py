
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