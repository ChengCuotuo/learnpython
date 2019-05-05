a_list = list(range(1, 100, 2))
print("100以内的奇数：")
print(a_list)
a_list = list(range(2, 100, 2))
print("100以内的偶数：")
print(a_list)

b_list = list((2, 3, 4))
b_list.append(9)
print(b_list)
b_list.pop()
print(b_list)
b_list.pop(0)
print(b_list)
b_list.append(5)
print(b_list)
b_list.pop(-2)
print(b_list)
#删除首次出现的指定元素，如果列表中没有需要删除的元素，就抛出异常
a_list = [1, 2, 3, 4, 5,6]
a_list.remove(3)
print(a_list)
print(a_list.index(4))
print(a_list.index(8))

a = [1, 2, 3]
print(id(a))

