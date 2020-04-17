#有序队列
def func(S):
    # your code here
    min_str = S
    for i in range(len(S)):
        S = S[1:] + S[0]
        if S < min_str:
            min_str = S
    output = min_str

    return output
     
S = eval(input())       #eval() 函数用来执行一个字符串表达式，并返回表达式的值
#print((S[0]))
print(func(S))