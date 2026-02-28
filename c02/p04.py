##########################################
####author:Anzilz1972
####date: 2026-2-28
####Python官网教程：4.更多控制流工具-函数注解
##########################################

####################################################################################
####函数注解是 Python 3.0+ 引入的特性，允许为函数参数和返回值添加任意的元数据。
####这些注解不会影响函数的运行，主要用于类型提示、文档、参数验证等。
import functools
from typing import List, Dict, Optional, Union, Tuple


##############################################################
####: function
def print_f_info(f: functools):
    """打印函数注解信息和文档信息

    """
    print(f'Funtion: {f.__name__}()\n   {f.__annotations__}\n\n   {f.__doc__}')
    print('-' * 100)


##############################################################
def greet(name: str) -> str:
    """注解初探
    
    'name: str':name的类型为str
    '-> str'   :函数返回值为str
        
    """
    return f"Hello, {name}"

#print(greet('world'))
print_f_info(greet)

##############################################################
def add(a: int, b: int) -> int:
    """注解再探

    a,b:integer
    return:integer
    """
    return a + b

#print(add(7,8))
print_f_info(add)

##############################################################
def divide(dividend: float, divisor: float) -> float:
    """除法函数"""
    return dividend / divisor

#print(divide(3.78,2.23))
print_f_info(divide)

##############################################################
def process_data(
        items: List[str],                     # 字符串列表
        config: Dict[str, int],               # 字符串到整数的字典
        timeout: Optional[float] = None,      # 可选的浮点数
        mode: Union[str, int] = "normal"      # 字符串或整数
) -> Tuple[bool, int]:                        # 返回布尔值和整数的元组
    """处理数据函数"""
    success = len(items) > 0
    return success, len(items)

result = process_data(["a", "b"], {"max": 10}, 5.0, 1)
print(result)  # 输出: (True, 2)
print_f_info(process_data)

##############################################################
def calculate(
        radius: "圆的半径,单位：米",
        precision: "计算精度,小数位数" = 2
) -> "返回圆的面积,单位：平米":
    """注解可以是任何表达式
    
    不仅仅是类型"""
    return round(3.14159 * radius ** 2, precision)
#print(calculate(10 , 2))
print_f_info(calculate)

##############################################################
def process(
        data: "重要数据，必须处理",
        weight: {"min": 0, "max": 100}
) -> {"Status": "success/error"}:
    """使用复杂表达式作为注解
    """
    return{"Status": "success" if weight > 50 else "error"}
print(process(11,77))
print_f_info(process)




















