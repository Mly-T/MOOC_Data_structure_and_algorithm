from pythonds.basic.stack import Stack

def func(lst1):
    s1, s2 = Stack(), Stack()
    for item in lst1:
        s1.push(item)
    lst2 = []
    while not s1.isEmpty():
        ### 在此进行代码填空 ###
        lst2.append(s1.peek())
    

    return lst2
 
# 测试
print(func([1, 3, 5, 7, 9]))