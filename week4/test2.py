#最近的请求次数
def func(mylist):
    # your code here
    temp = mylist
    var1 = 0

    for i in range(len(mylist)-1):
        temp[i] = mylist[i] - 10000
       


    

    output = temp


    return output
     
mylist = eval(input())
print(func(mylist))
