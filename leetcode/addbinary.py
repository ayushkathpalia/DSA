def addBinary(a, b):
    res = ""
    carry = 0
    
    a,b = a[::-1],b[::-1]
    for i in range(max(len(a),len(b))):
        digitA = int(a[i])if i < len(a) else 0
        digitB = int(b[i])if i < len(b) else 0
        total = digitA + digitB +carry
        char = str(total % 2)
        print(char)
        res+=char
        carry = total//2
        print(carry)
    if carry:
        res = "1"+res
    print(res)

addBinary("1010","1011")