#检查输入的左右括号数量是否匹配
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

input_0 = input()
check_0 = Stack()
for i in input_0:
    if check_0.isEmpty():
        check_0.push(i)
        continue
    if check_0.peek() == i:
        check_0.pop()
    else:
        check_0.push(i)
print(''.join(check_0.items))



