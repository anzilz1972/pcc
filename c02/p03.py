#####################################
####author:Anzilz1972
####date: 2026-2-25
####Python官网教程：4.更多控制流工具-lambda函数
#####################################



##############################################################
####平方计算
square = lambda x: x**2
print(square(5))

#a + b
add =lambda a, b: a + b
print(add(7,3))


##############################################################
####自定义排序
students = [
    {'name': 'Alice' , 'grade': '89'},
    {'name': 'Bob' , 'grade': '79'},
    {'name': 'Charlie' , 'grade': '93'},
    {'name': 'Jhon' , 'grade': '98'}
]

#按成绩高低排序
students_sorted_bygrade = sorted(students, key= lambda s: s['grade'], reverse= True)
print(students_sorted_bygrade)

#按名字长度排序
students_sorted_bynamelen = sorted(students, key= lambda s: len(s['name']))
print(students_sorted_bynamelen)


##############################################################
####过滤数据：filter(func, iterable)用于过滤序列，保留使函数返回 True的元素
numbers = [1,2,3,4,5,6,7,8,9,10]

#过滤所有偶数
even_numbers = list(filter(lambda x: x % 2 ==0, numbers))
print(even_numbers)

#过滤出大于5的数
greater_than_five = list(filter(lambda x: x > 5, numbers))
print(greater_than_five)



##############################################################
####map(func, iterable)将函数应用于序列的每一个项，并返回结果迭代器

#将numbers列表中每个数字变为平方，生成新列表
squares = list(map(lambda x: x ** 2 , numbers))
print(squares)

#将两个列表的对应位置相加，生成新列表
list_a = [2,4,6]
list_b = [5,7,3]
sum_list = list(map(lambda a,b: a + b , list_a, list_b))
print(sum_list)

#配合条件生成推导式
data = [10,15,20,None,25,None,30]
cleaned = list(map(lambda x: 0 if x is None else x, data))
print(cleaned)












