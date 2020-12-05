# Python Class Progrom

## 一、随机数生成
> 生成一个包含50个随机整数的列表，删除所有奇数

```python
import random 
lst1 = [random.randint(0, 100) for i in range(50)]
lst2 = [i for i in lst1 if i%2 == 0]

print('随机生成的整数：', lst1, '\n\n偶数：', lst2)
```

- 使用列表推导式生成随机整数列表
- 使用列表推导式加条件判断去除奇数


[![random.png](https://s3.ax1x.com/2020/11/28/Dy76OA.png)](https://imgchr.com/i/Dy76OA)


## 二、简易计算器
> 用Python模拟简单的计算器，实现Python中的基本计算运算，运算符包括：+ - * % ** // ... 输入非法时提示重新输入

[![cal.png](https://s3.ax1x.com/2020/11/28/D6yG80.png)](https://imgchr.com/i/D6yG80)

#### 参照
> 复刻系统自带计算器 功能基本一致

[![cal.png](https://s3.ax1x.com/2020/12/04/Dqs6ZF.png)](https://imgchr.com/i/Dqs6ZF)

#### 核心代码


```python
try:
    result = eval(self.display.get())
    print(result, type(result))
    self.display.delete(0, END)
    self.display.insert(END, '%s' %result)
except:
    self.display.delete(0, END)
    # self.display.insert(END, 'Err.')
    tm.showwarning('Warning', '无法计算，请重新输入运算符！')
```
- 利用eval( )方法 直接求解用户输入表达式
- 利用Python标准异常处理 排除表达式无法计算的情况


## 三、学生信息管理系统
> 信息包括学号、姓名、3门成绩，方法有输出、求全班平均成绩、按总成绩排序，将学生信息存储到文件里面，并且可以从文件中读取

### A. 基本写法

#### 学生类
- ##### 属性
	- 学号
	- 姓名
	- 分数

- ##### 方法
	- 设置方法
	- 获取方法
	- 功能方法 ( 求和 求平均 )
	- 查看方法


#### 班级类
- ##### 属性
	- 班级列表 ( 用于存储学生类 ) 

- ##### 方法
	- 增加方法
	- 获取方法
	- 功能方法 ( 求和 求平均 排序 )
	- 文件方法
	- 查看方法

##### 主要代码

**学生类：**
```python
def get(self):
	return [self.__num, self.__name, self.__grade0, self.__grade1, self.__grade2]
```
返回类属性的值

```python
def set(self):
	self.__num = int(input('num: '))
	self.__name = input('name: ')
	self.__grade0 = float(input('grade1: '))
	self.__grade1 = float(input('grade2: '))
	self.__grade2 = float(input('grade3: '))
```

- 设置方法
- input函数获取用户输入值

```python
def total(self):
    return sum(self.get()[2:])
```

- get方法返回属性值
- 利用列表切片
- 截取成绩位
- 表求和函数sum求和

```python
def average(self):
    return self.total() / 3
```

- total方法获取总分 直接除以科目数得平均分

**班级类：**
```python
def __init__(self):
    super().__init__()
    self.__cls_ = []
```
- 双下划线私有化属性
- cls属性必须私有化 防止外界直接访问修改

```python
def add(self, option=None):
    if option:
        item = stu(option[0], option[1], float(option[2]), float(option[3]), float(option[4]))
    else:
        item = stu()
        item.set()
    
    self.__cls_.append(item)
```
- 形参option用于 数据文件导入时所用行参
- 条件判断语句 用于判断是否用户输入或文件输入
- 最后将学生类存入 __cls 的列表

```python
def gets(self):
    return [i.get() for i in self.__cls_]
```
- 列表推导式获取 __cls_ 列表中学生类对应的值
- get( ) 为学生类的方法

```python
def average(self):
    av = [i.average() for i in self.__cls_]
    return sum(av)/len(av)
```
- 列表推导式 将__cls_属性中所有学生平均分 创建成列表
- 利用列表求和函数在除以列表长度既得总平均分

```python
def sort(self):
    def takeTotal(elem):
        return elem.total()
    self.__cls_.sort(key=takeTotal, reverse=True)
```
- 利用sort( ) 列表排序方法 参照值为每个学生的总分
- takeTotal方法 取得总分

```python
def savefile(self):
    with open('test.txt', 'w+') as f:
        for item in self.gets():
            item = map(lambda x:str(x), item) # 将列表的元素转化为str
            info = ','.join(item)+'\n'
            f.write(info)
```

- gets( ) 方法 将所有学生的所有信息组合为一个列表 每个学生的信息为一个子列表
- join 方法 将列表拼接为字符串 ',' 以逗号隔开
- join 方法 要求列表对象为 str 所有必须将列表元素转化为str
- map( )配合 lambda表达式 快速将列表的元素转化为str

```python
def openfile(self):
    with open('test.txt', 'r+') as f:
        for i in f.readlines():
            item = i[:-1].split(',') # -1：换行符
            self.add(item)
```
- readlines 方法 按行读取数据文件
- 将每行以 ',' 分割转化为列表
- 由于每行最后一个字符为换行符 利用字符串切片将其排除
- add方法如上述 形参为option 用于文件数据导入

### B. 进阶写法
#### 基本思路
[![Dqclx1.png](https://s3.ax1x.com/2020/12/04/Dqclx1.png)](https://imgchr.com/i/Dqclx1)

#### 界面及功能
[![stuman1.png](https://s3.ax1x.com/2020/12/04/Dq6g3R.png)](https://imgchr.com/i/Dq6g3R)

## 四、求质因数
>  输入一个整数，分解该整数的质因数


[![factor0.png](https://s3.ax1x.com/2020/11/28/Dy5YUU.png)](https://imgchr.com/i/Dy5YUU)


##### 输入1提示
[![factor1.png](https://s3.ax1x.com/2020/11/28/DyHNcQ.png)](https://imgchr.com/i/DyHNcQ)

##### 输入质数提示
[![factor2.png](https://s3.ax1x.com/2020/11/28/DyH69U.png)](https://imgchr.com/i/DyH69U)

#### 核心代码

```python
lst = []
while num > 1:
	for i in range(2, num + 1):
		if num % i == 0:
			num //= i
			lst.append(str(i))
			break
```


- 创建空列表用于存储分解出来的质因数
- while 配合 for 循环 每次只求第一个质因数，例如
<br/>12 = 2 x 6 --->  2  <br/>6 = 2 x 3 --->  2<br/>3 = 3 x 1 --->  3<br/>求得12 = 2 x 2 x 3
- 随着计算数字会越来越小 时间复杂度为Logn



## 四、TB图片爬取工具



