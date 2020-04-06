# a= int(input(""))
# b= int(input(""))
# if b == 0:
#     print("NA")
# else:
#     print('%.4f' % float(a/b))
##########################
# m,n = input().split()
# m = int(m)
# n = int(n)
# for i in range(m):
#     print("*"*n)
# ##########################
n=input().split(" ")
for i in range(len(n)):
    n[i] = int(n[i])
n.sort(key=lambda x: (x >= 0, abs(x)))
print(n[0])



