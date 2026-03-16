##########################################
####author:Anzilz1972
####date: 2026-3-16
####Python编程：从入门到实践
####研究dis 模块
##########################################

#####################################
#dis模块是 Python 的反汇编器，用于将 Python 字节码转换为人类可读的形式。
#它对于理解 Python 代码的执行细节、性能分析和深入学习 Python 内部机制非常有帮助。
#  基本功能:
#1 将 Python 字节码转换为可读的助记符
#2 显示代码对象的内部结构
#3 帮助理解 Python 解释器的工作原理
#4 用于性能分析和优化

import dis


#####################################
class Calculator:
    def __init__(self, value=0):
        self.value = value

    def add(self, n):
        self.value += n
        return self.value

print("\n=== 反汇编 Calculator 类 ===")
dis.dis(Calculator)
#print("\n=== Calculator类 代码对象信息===")
#dis.show_code(Calculator)  //类不能调用 dis.show_code(),错误
    
#####################################
def iter_list():
    """遍历列表
    调用dis模块观察行为
    """
    magicians = ['alice','david','mary','Jhon']
    for magician in magicians:
        print(magician)
    return
print("\n===  iter_list() 函数 代码对象信息 ===")
dis.show_code(iter_list)
print("\n=== 反汇编 iter_list() 函数 ===")
dis.dis(iter_list)
print("\n===  iter_list() 函数 指令详情 ===")
for instr in dis.get_instructions(iter_list):
    print(f"{instr.opname:20} {instr.argrepr:20} | "
          f"opcode={instr.opcode:3d}, "
          f"arg={instr.arg}, "
          f"offset={instr.offset}")

#####################################
def add_ab(a:int, b:int) -> int:
    """反汇编函数
    a,b:integer
    return:integer
    """
    result  = a + b
    return result

print("\n===  add_ab函数 代码对象信息 ===")
dis.show_code(add_ab)
print("\n=== 反汇编 add_ab 函数 ===")
dis.dis(add_ab)
print("\n===  获取add_ab函数 指令详情 ===")
for instr in dis.get_instructions(add_ab):
    print(f"{instr.opname:20} {instr.argrepr:20} | "
          f"opcode={instr.opcode:3d}, "
          f"arg={instr.arg}, "
          f"offset={instr.offset}")


#####################################
### 反汇编代码字符串
codestr = """
x = 10
y = 20
z = x + y
print(z)
"""
#print("\n=== 反汇编代码字符串 ===")
#dis.dis(codestr)


###################################################################
##                        以下观察字节码指令                       ##
###################################################################
def load_store_demo():
    """观察:LOAD/SAVE 指令
    """
    # LOAD_CONST 加载常量
    # LOAD_FAST  存储到局部变量
    x = 10       #LOAD_CONST, STORE_FAST
    y = 20       #LOAD_CONST, STORE_FAST
    
    # LOAD_FAST, LOAD_FAST 加载局部变量
    # BINARY_ADD 调用操作符 
    # STORE_FAST 存储到局部变量
    z = x + y    #LOAD_FAST, LOAD_FAST, BINARY_ADD, STORE_FAST

    #LOAD_GLOBAL: 加载全局变量
    result = len([1,2,3,4,5,6])  #LOAD_GLOBAL(len)

    #LOAD_FAST: 加载局部变量
    return z

print("\n=== 加载/存储指令 ===")
dis.dis(load_store_demo)


def operations_demo():
    """观察：操作符( operations: +-*/% **) 
    """
    a = 100
    b = 3
    
    # 基本运算
    add = a + b     #BINARY_ADD
    sub = a - b     #BINARY_SUBSTRACT
    mul = a * b     #BINARY_MULTIPLY
    div = a / b     #BINARY_TRUE_DIVIDE
    mod = a % b     #BINARY_MODULO
    pow = a ** b    #BINARY_POWER

    # 比较运算
    cmp = a > b     #COMPARE_OP

    return add, sub, mul, div, mod, pow, cmp

print("\n=== 运算指令 ===")
dis.dis(operations_demo)


def control_flow_demo(n:int)-> tuple:
    """观察: 控制流指令
    """

    #JUMP_ABSOLUTE: 绝对跳转
    #POP_JUMP_IF_FALSE: 条件为假时跳转
    if n > 0:
        result = "positive number"
    else:
        result = "not positive number"

    #SETUP_LOOP, GET_ITER, FOR_ITER: for循环
    total = 0
    for i in range(n):
        total += i

    #WHILE 循环
    while total > 0:
        total -= 1
    
    return result, total

print("\n=== 控制流指令 ===")
dis.dis(control_flow_demo)








