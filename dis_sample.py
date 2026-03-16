##########################################
####author:Anzilz1972
####date: 2026-3-16
####Python编程：从入门到实践
####dis模块应用实践:对生成list的三种函数进行性能分析
##########################################
import dis
import timeit

list_size = 100000

#列表推导式生成 list
def creat_list1():
    return [x**2 for x in range(list_size)]

#map函数生成 list
def creat_list2():
    return list(map(lambda x: x**2, range(list_size)))

#普通循环生成 list
def creat_list3():
    result = []
    for x in range(list_size):
        result.append(x**2)
    return result

#print("\n=== 字节码对比 ===")

print("\n写法1 - 列表推导式:")
dis.dis(creat_list1)

print("\n写法2 - map函数:")
dis.dis(creat_list2)

print("\n写法3 - 普通循环:")
dis.dis(creat_list3)

#性能测试
print(f"\n=== 性能测试 , List Size:{list_size} ===")
for i, func in enumerate([creat_list1, creat_list2, creat_list2], 1):
    time = timeit.timeit(func, number=1000)
    print(f"Creat list Mothed{i}: {time:.6f} second.")











