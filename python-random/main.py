import random 
lst1 = [random.randint(0, 100) for i in range(50)]
lst2 = [i for i in lst1 if i%2 == 0]

print('随机生成的整数：', lst1, '\n\n偶数：', lst2)
