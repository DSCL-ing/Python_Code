
## 生成器函数:
## 带yield关键字的的函数就是生成器函数

## 语法关键字: yield,send()

### yield:
### 1.具有return的返回功能,但不终止程序
### 2.返回生成器(只返回一次)
#### 用途:节省内存(模拟迭代器可以将代码分段处理)

### send(参数):
### 1.将参数传给接收yield的变量
### 2.具有return的返回功能,但不终止程序
### 3.返回生成器(只返回一次)
### 4.注:生成器函数刚启动时不可使用send,因为生成器函数只是返回生成器,还没开始执行(到第一个yield)

def fun():
    print("yield1")
    a = yield "zhangsan"        ## yield1
    print("yield2","yield1=",a)
    b = yield "lisi"            ## yield2
    print("yield3","yield2=",b)
    yield "end"                 ## yield3

gen = fun()     ## 并不执行代码,创建并返回生成器给gen,然后暂停代码执行,保存到内存中等待next/send(后面的所有代码都是如此)
print(gen)      ## 打印结果: <generator object fun at 0x0000022950846180>
ret = gen.__next__()  ## 执行到第一个yield,然后返回yield1的值; 注:第一个yield必须使用next,因为还没开始执行,没有变量接收send的参数
print(ret)      ## 打印结果: zhangsan
ret = gen.send("传给a的值") ## 将参数传给a,,然后走到下一个yield(yield2),并返回yield的值
print(ret)
ret = gen.send("传给b的值")
print(ret)
## ret = gen.send("") ## StopIteration



