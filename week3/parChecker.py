#检查输入的左右括号数量是否匹配
from pythonds.basic.stack import Stack

def parChecker(symbolString):
    symbolString = symbolString.replace(" ", "")  #去掉字符串中的空格
    print(symbolString)
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,symbol):
                    balanced = False
        index = index + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open,close):
    opens = "([{"
    closers = ")]}"
#    print(opens.index(open) == closers.index(close))
    return opens.index(open) == closers.index(close)

#print(parChecker('{{([][])}()}'))
#print(parChecker('[{()]'))
print("*"*10)
print(parChecker('{{   )]}'))