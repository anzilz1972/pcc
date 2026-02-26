#####################################
####author:Anzilz1972
####date: 2026-2-25
####Python官网教程：4.更多控制流工具-函数
#####################################
def draw_line():
    """ Print a line use '*' """
    print('*' * 100)
    return

def fib(n):
    """ Print a Fibonacci series less than n. """
    a, b = 0, 1
    while a < n:
        print(a, end = ' ')
        a, b = b ,a + b

def fib2(n):
    """Return a list containing the Fibonacci series up to n"""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result

def calculate(a, b):
    """通过元组tuple返回多个值"""
    """本函数返回和、差、积"""
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    return addition , subtraction , multiplication

def get_student_inf():
    """返回字典信息"""
    student = {
        'name' : 'JadeBlack',
        'age' : 54,
        'courses' : ['Computer Science','Data Structer','English']
    }
    return student


def ask_ok(prompt, retries=3, reminder='Please try again!'):
    """为函数制定默认值参数"""
    while True:
        reply = input(prompt)
        if reply in {'y','ye','yes'}:
            return True
        if reply in {'n','no','nop','nope'}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    """ kwarg=value形式的关键字形参"""
    """ 函数调用时，关键字参数必须跟在位置参数后面。"""
    """ 所有传递的关键字参数都必须匹配一个函数接受的参数​，关键字参数的顺序并不重要。"""
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!\n")

def cheeseshop(kind, *arguments, **keywords):
    """ *args形参和**keywords形参 """
    """ *args形参,必须在**keywords形参之前,接收一个元组tuple,包含形参列表之外的位置参数 """
    """ **keywords形参,接收一个字典，该字典包含与函数中已定义形参对应之外的所有关键字参数 """
    print("--Do you have any", kind, "?")
    print("--I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print('-' * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])
    print('\n')



##############################################################
### call fib2()
'''
num = int(input('Please enter a integer bigger than 2:'))
print('The Fibonacci series:')
res = fib2(num)
for n in res:
    print(n, end= ' ')
draw_line()
'''

##############################################################
### call calculate()
input_str =  input("Please input two integer:")
num1, num2 = map(int, input_str.split())
results = calculate(num1 , num2)
print(results)
sum_val, diff_val, prod_val = results
print(sum_val, diff_val, prod_val)
print(type(results))
draw_line()

##############################################################
### call get_student_inf()
info = get_student_inf()
print(f'{info['name']} {info['age']} {info['courses']}')
print(info)
print(type(info))
draw_line()

##############################################################
### call parrot()
parrot(1000)                                          # 1 个位置参数
parrot(voltage=1000)                                  # 1 个关键字参数
parrot(voltage=1000000, action='VOOOOOM')             # 2 个关键字参数
parrot(action='VOOOOOM', voltage=1000000)             # 2 个关键字参数
parrot('a million', 'bereft of life', 'jump')         # 3 个位置参数
parrot('a thousand', state='pushing up the daisies')  # 1 个位置参数，1 个关键字参数

##############################################################
### call cheeseshop()
cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper = "Michael Palin",
           client = "John Cleese",
           sketch = "Cheese Shop Sketch")


##############################################################
### call ask_ok()
ask_ok('Do you really want to quit?')
draw_line()


