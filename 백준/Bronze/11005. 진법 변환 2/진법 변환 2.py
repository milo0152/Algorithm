bignum, num = map(int, input().split())

text = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = ""

while 1:
    i = bignum % num
    result = text[i] + result
    bignum = bignum // num
    
    if bignum == 0:
        break
    

print(result)