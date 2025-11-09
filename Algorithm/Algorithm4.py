n = int(input())

def count(n):
    num = 0
    num1 = n
    
    while True:
        num += 1
        n = (n % 10) * 10 + ((n // 10 + n % 10) % 10)
        
        if n == num1:
            break
    
    return num

print(count(n))