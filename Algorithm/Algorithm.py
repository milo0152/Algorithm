n, m = input().split()

n = int(n)
m = int(m)

num = 0
num1 = 0

for i in range(n):
    num = (n-i) * (10**i)
    num1 = num + num1

basket = list(str(num1))


for j in range(m):
    n, m = input().split()

    n = int(n) - 1
    m = int(m) - 1

    basket[n], basket[m] = basket[m], basket[n]

print(basket)
