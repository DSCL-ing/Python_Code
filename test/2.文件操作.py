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
## 需要组合模式: "rb","wb","ab"等才能够使用 //一般用于处理各类非文本文件的读写
# f = open("b.txt",mode="b",encoding = "utf-8")   # ValueError: binary mode doesn't take an encoding argument
ff = open("b.txt",mode="bw")
ff.close()

## 还有r+,w+等,+就是扩展,r+就是r扩展读... 可读性很差,不推荐,基本的rwab都够用了
### 注意顺序,r+是读在先,即必须先读后才能写

f.close()    # 关闭句柄

## 类似智能指针的东西,适用各种句柄类如网络,线程等
with open("b.txt",mode="r",encoding="utf=8") as f1:
    for line in f1:
        f1.readline()
    ### <---这里自动加上f1.close()

### 打开多个文件
with open("test.txt",mode="r",encoding="utf-8") as f1,\
     open("b.txt",mode="a",encoding="utf-8") as f2:
    for line in f1:
        f2.write(line)



### 应用:修改文件内容
### 逻辑:将源文件内容读取到内存中,修改后写入到新文件中,然后删除源文件,重命名新文件(最省内存,可以读一行写一行)
### 问题? 写回源文件OK不?即r+ //局限,内存不够大就很麻烦,必须一次读完

import os       ## 导入OS模块,用于调用各种系统接口

with open("b.txt",mode="r",encoding="utf-8") as fb,\
     open("c.txt",mode="w",encoding="utf-8") as fc:
    for line in fb:
        if("d" in line):
            line=line.replace("d","屯") ## 将一行中的b改成屯
        fc.write(line)
os.remove("b.txt")
os.rename("c.txt","b.txt")
        
