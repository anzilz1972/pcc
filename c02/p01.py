#####################################
####author:Anzilz1972
####date: 2026-2-25
####Python官网教程：4.更多控制流工具
#####################################


#### if 语句
#x = int(input("Please enter an integer:\n"))
x = 0
if x < 0:
    x = 0
    print('Negative changed to zero\n')
elif x == 0:
    print('Zero\n')
elif x == 1:
    print('Single\n')
else:
    print ('More\n')

#### for 语句
words = ['cat','bird','lion','animal']
for word in words:
    print(word, len(word))


students = {'David':19,'Mary':18,'Jane':22,'Tom':20,'Hanks':21}

print(students.keys())
print(students.values())
print(students.items())
for name,age in students.items():
    print(f'{name} age:{age}')

#### for 循环的else 子句
for n in range (2,30):
    for x in range (2,n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        #循环未找到一个因数，N是质数
        print(n, 'is a primer number.')








    

