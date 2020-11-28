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

[![random.png](https://s3.ax1x.com/2020/11/28/Dy4oh4.png)](https://imgchr.com/i/Dy4oh4)



## 二、简单计算器
> 用Python模拟简单的计算器，实现Python中的基本计算运算，运算符包括：+ - * % ** // ... 输入非法时提示重新输入


## 三、学生信息管理系统
> 信息包括学号、姓名、3门成绩，方法有输出、求全班平均成绩、按总成绩排序，将学生信息存储到文件里面，并且可以从文件中读取



## 四、TB图片爬取工具

