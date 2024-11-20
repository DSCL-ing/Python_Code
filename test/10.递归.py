
## 和其他语言一样，要有递归出口即可

def func(a):
    if(a == 0):
        return
    print(a)
    func(a-1)

func(10)


### 遍历文件夹
print()
import os

def readpath(path,level):   
    lst = os.listdir(path)  ## 遍历获取当前路径的目录/文件名,没有路径前缀
    for name in lst:
        real_path = os.path.join(path,name) ## 拼接成绝对路径 ## C:\User\chj\a.txt
        if os.path.isdir(real_path):
            # 是文件夹
            print("\t"*( level-1 ),"└---"*(1 if level>0 else 0),name)
            readpath(real_path,level+1)
        else:
            # 是文件
            print("\t"*( level -1),"└---"*(1 if level>0 else 0),name)

readpath("..",0)