txt = input()
x = 0
result = ""

for i in txt:
    if i == 'X':
        x += 1
    else:
        if x % 2 == 1:
            print(-1)
            exit()
        else:
            result += "AAAA" * (x // 4)
            result += "BB" * ((x % 4) // 2)
            x = 0
            result += "."
            
if x % 2 == 1:
    print(-1)
    exit()

result += "AAAA" * (x // 4)
result += "BB" * ((x % 4) // 2)

print(result)