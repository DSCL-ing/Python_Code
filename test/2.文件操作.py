## r模式

### f为文件句柄(程序与文件互相连接的管子)
### 管道方式读,每次读文件指针都会向后移动
f = open("./test.txt","r",encoding="utf-8") 

### 1.read()  ## 默认读取全部内容
# print(f.read())

### 2.read(字符数)
# print(f.read(3))

### 3.readline()  : 一次读取一行
# print(f.readline())

### 4.for循环读(常用)
# for line in f:
#    print(line.strip()) ## strip(),默认去掉换行


## w模式
### w模式,只写模式,会重新创建文件
# f = open("b.txt",mode="w",encoding="utf-8")
# f.write("hello ")   ## 不自带换行,需要自己带
# f.write("world")    ## 
# f.write("\n换行")

## a模式,append
### 追加,不会重新创建文件,如果不存在则会创建文件
# f = open("b.txt",mode="a",encoding = "utf-8")
# f.wirte("追加")

## b模式,bytes/binary
## 一般处理非文本文件,不能指定encoding
## 组合模式: "rb","wb","ab",一般用于处理各类文件的读写
# f = open("b.txt",mode="b",encoding = "utf-8")   # ValueError: binary mode doesn't take an encoding argument
f = open("b.txt",mode="b")
