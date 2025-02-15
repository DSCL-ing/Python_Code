
## 迭代器：对遵循可迭代协议(统一的迭代规则）的类型，其可迭代协议的实现，就是迭代器

## 可迭代类型：
### 找print(dir(类型)) 中是否存在__iter__


## __iter__()
## 可迭代类型通过__iter__取得迭代器
lst = {1,2,3}
it = lst.__iter__()

## __next__()
## 迭代器当前结点的下一个
it.__next__()   ## 访问下一个元素

## 内置函数iter() 和 next()
## 通过内置函数获取迭代器,和迭代
it = iter(lst)
next(it)    ## it指向下一个


## 模拟for-each循环
it = iter(lst)
while True:
    try:
        obj = next(it)
        print(obj)
    except StopIteration:
        break

