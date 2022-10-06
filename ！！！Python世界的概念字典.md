---


## title: Python世界的概念——字典<br />date:  2020-01-13  19:45:08<br />tags: Python<br />categories: knowledge base

[TOC]
## pip

### 一、pip是什么？

> pip is the [package installer](https://packaging.python.org/en/latest/current/) for Python. You can use pip to install packages from the [Python Package Index](https://pypi.org/) and other indexes.


pip 是 Python 包管理工具，该工具提供了对Python 包的查找、下载、安装、卸载的功能。

### 二、如何安装pip？

python在python3.x以上的发行版本中，都是自带pip的。

#### 1. Linux（Debian及其衍生发行版）环境安装pip

**安装pip：**

```
sudo apt install python-pip
```

如果是**pip3**命令修改为：【sudo apt install python3-pip】

**如果安装的是pip想换成pip3怎么卸载？**

```csharp
python -m pip uninstall pip
    
sudo apt-get remove python-pip python-pip
```

**在中国使用pip下载速度很慢怎么办？ **

使用国内pypi镜像源提高pip下载速度

**pypi国内镜像源：**

新版ubuntu要求使用https源，要注意。

-  清华：[https://pypi.tuna.tsinghua.edu.cn/simple](https://links.jianshu.com/go?to=https%3A%2F%2Fpypi.tuna.tsinghua.edu.cn%2Fsimple) 
-  阿里云：[http://mirrors.aliyun.com/pypi/simple/](https://links.jianshu.com/go?to=http%3A%2F%2Fmirrors.aliyun.com%2Fpypi%2Fsimple%2F) 
-  中国科技大学 [https://pypi.mirrors.ustc.edu.cn/simple/](https://links.jianshu.com/go?to=https%3A%2F%2Fpypi.mirrors.ustc.edu.cn%2Fsimple%2F) 
-  华中理工大学：[http://pypi.hustunique.com/](https://links.jianshu.com/go?to=http%3A%2F%2Fpypi.hustunique.com%2F) 
-  山东理工大学：[http://pypi.sdutlinux.org/](https://links.jianshu.com/go?to=http%3A%2F%2Fpypi.sdutlinux.org%2F) 
-  豆瓣：[http://pypi.douban.com/simple/](https://links.jianshu.com/go?to=http%3A%2F%2Fpypi.douban.com%2Fsimple%2F) 

**临时使用：pip install 库名 -i 镜像地址**

如使用豆瓣源下载numpy

```cpp
pip install numpy -i http://pypi.douban.com/simple/
```

#### 2. Windows环境

在windows下安装python3后，自带pip工具，一般情况下不会出现pip安装和卸载的情形。

### 三、pip命令如何查看安装的库？

查看pip安装库的命令：list

```cpp
pip3 list
```

## Pypi

**The Python Package Index (PyPI)** is a repository of software for the Python programming language.

PyPI(Python Package Index)是python官方的第三方库的仓库，所有人都可以下载第三方库或上传自己开发的库到PyPI。PyPI推荐使用pip包管理器来下载第三方库。

## 运行环境的配置
## Jupyter NoteBook

### 安装Jupyter（国内清华tuna源）

> pip3 install Jupyter -i [https://pypi.tuna.tsinghua.edu.cn/simple](https://pypi.tuna.tsinghua.edu.cn/simple)


### 卸载Jupyter Notebook

> pip3 uninstall notebook


### 在windows系统下运行Jupyter Notebook

在cmd命令提示窗口下运行：

> Jupyter Notebook


## 程序结构

循环结构

1. while循环
```matlab
while (循环判断) :
  	语句1


```
```matlab
i =0
while (i<6) : ### i<A 则循环到（A-1）就跳出循环，共循环了（A-1）次
	print("做了",i,"俯卧撑")
	i=1+i

输出：
做了 0 俯卧撑
做了 1 俯卧撑
做了 2 俯卧撑
做了 3 俯卧撑
做了 4 俯卧撑
做了 5 俯卧撑


------------------
(program exited with code: 0)

请按任意键继续. . .

```
（i<=6）时候
```matlab
i =0
while (i<=6) : ### i<=A 则循环到A跳出循环，共循环了A次
	print("做了",i,"俯卧撑")
	i=1+i
做了 0 俯卧撑
做了 1 俯卧撑
做了 2 俯卧撑
做了 3 俯卧撑
做了 4 俯卧撑
做了 5 俯卧撑
做了 6 俯卧撑


------------------
(program exited with code: 0)

请按任意键继续. . .

```
| i =0  while(i<A) |  A次 |
| --- | --- |
| i =0 while(i<=A) | A+1次 |
| i=B  while(i<A)  | (A-B)次 |
| i=B while（i<=A） |  A-B+1次 |

