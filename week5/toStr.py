def toStr(n,base):
    converString = "0123456789ABCDEF"
    if n < base:
        #print(type(converString[n]))
        return converString[n]
    else:
        return toStr(n//base,base) + converString[n%base]

print(toStr(135,3))
