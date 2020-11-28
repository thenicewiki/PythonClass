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


[![Dy76OA.png](https://s3.ax1x.com/2020/11/28/Dy76OA.png)](https://imgchr.com/i/Dy76OA)


## 二、简单计算器
> 用Python模拟简单的计算器，实现Python中的基本计算运算，运算符包括：+ - * % ** // ... 输入非法时提示重新输入


## 三、学生信息管理系统
> 信息包括学号、姓名、3门成绩，方法有输出、求全班平均成绩、按总成绩排序，将学生信息存储到文件里面，并且可以从文件中读取

## 四、求质因数
>  输入一个整数，分解该整数的质因数


[![factor.png](https://s3.ax1x.com/2020/11/28/Dy5YUU.png)](https://imgchr.com/i/Dy5YUU)

Main Code
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
- while 配合 for 循环 每次只求第一质因数，例如
	12 = 2 x 6 --->  2
	6 = 2 x 3 --->  2
	3 = 3 x 1 --->  3
	
	求得12 = 2 x 2 x 3


	



## 四、TB图片爬取工具

