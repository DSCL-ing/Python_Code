## 文件读

### f为文件句柄(程序与文件互相连接的管子)
f = open("./test.txt","r",encoding="utf-8") 

### read()  ## 默认读取全部内容
print(f.read())