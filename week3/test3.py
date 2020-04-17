#强迫症老板和他的洗碗工
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

def washdishes(s):
    stack = []  #用list做的，没用stack
    for i in s:
        if len(stack) == 0:
            stack.append(i)
        elif i < stack[-1]: # 判断是否往前取编号小的盘子
            if not i + 1 in stack: # 判断编号大1的盘子是否已经被取走
                return 'No'
            else:
                stack.append(i)
        else:
            stack.append(i)
    return 'Yes'


dish_index = []
for i in input():
    dish_index.append(i)
#print(type(dish_index))
print(washdishes(list(map(int, dish_index))))
