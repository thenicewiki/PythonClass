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



## 简单计算器
> 用Python模拟简单的计算器，实现Python中的基本计算运算，运算符包括：+ - * % ** // ... 输入非法时提示重新输入


