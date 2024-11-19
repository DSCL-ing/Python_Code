## 闭包:内层函数对外层函数的变量的使用
### 作用1:可以让一个变量封锁起来,外界只能看到,但是无法修改
### 作用2:使变量常驻内存,不被回收(原因:如果被回收,那么inner就无法正常调用了;要保证inner能够正常调用,被闭包的变量必须不能被回收)
print()
print("## 闭包")
def fun():
    a = 10          ## 外界无法访问这个变量
    def inner():
        print(a)    ## 内部函数可以访问
        return a    ## 含可以返回他的值
    return inner    ## 返回这个函数,让外界可以安全访问

fn = fun()
fn()    ## 函数外访问到了函数的局部变量


## 装饰器

### 原始写法
# def add():
    # print("add")
# 
# def wrapper(fn):    ## 记录的add函数的地址
    # def inner():
        # print("在fn前做某事")
        # fn()
        # print("在fn后做某事")
    # return inner
# 
# add = wrapper(add)  ## add变量指向inner函数地址
# add()


### 语法糖写法 + 接收任意参数 + 返回值
print()
print("### 装饰器语法糖")
def wrapper(fn):    ## 记录的add函数的地址
    def inner(*args,**kwargs):      ## 聚合
        print("在fn前做某事")
        ret = fn(*args,**kwargs)            ## 打散
        print("在fn后做某事")
        print()
        return ret
    return inner

@wrapper    ## 简化了 add = wrapper(add) 这部分
def add():
    print("add")

@wrapper
def delete(name):
    print(name)


@wrapper
def find(name,age):
    print(name,age)
    return True

add()
delete("zhangsan")
ret = find("lisi",18)
print(ret)

'''以上为通用装饰器的写法'''

### 装饰器的应用
#### 高阶装饰器，层叠/嵌套装饰器
print()
def wrapper1(fn):
    def inner(*args,**kwargs):
        print("wrapper1_before:")
        ret = fn(*args,**kwargs);
        print("wrapper1_after")
        return ret
    return inner

def wrapper2(fn):
    def inner(*args,**kwargs):
        print("wrapper2_before:")
        ret = fn(*args,**kwargs);
        print("wrapper2_after")
        return ret
    return inner

def wrapper3(fn):
    def inner(*args,**kwargs):
        print("wrapper3_before:")
        ret = fn(*args,**kwargs);
        print("wrapper3_after")
        return ret
    return inner

@ wrapper3
@ wrapper2
@ wrapper1  ## 就近原则，一层套一层
def fun():
    print("fun")

fun()

### 结果：
"""
wrapper3_before:
wrapper2_before:
wrapper1_before:    
fun
wrapper1_after
wrapper2_after
wrapper3_after
"""



## 带有参数的装饰器
print()
print("## 带有参数的装饰器")

def wrapper_out(name):
    if name == 1:
        def wrapper1(fn):
            def inner(*args,**kwargs):
                print("wrapper1_before:")
                ret = fn(*args,**kwargs);
                print("wrapper1_after")
                return ret
            return inner
        return wrapper1     ## 返回装饰器的地址
    elif name == 2:
        def wrapper2(fn):
            def inner(*args,**kwargs):
                print("wrapper2_before:")
                ret = fn(*args,**kwargs);
                print("wrapper2_after")
                return ret
            return inner
        return wrapper2

@wrapper_out(1) ## 根据参数解析得到对应的装饰器地址,然后再与@组合成装饰器
def fun1():
    print("func1")
            
@wrapper_out(2)
def fun2():
    print("func2")

fun1()
fun2()
