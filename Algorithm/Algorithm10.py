tkfka = int(input())
time = list(map(int, input().split()))

for i in range(tkfka):
    for j in range(tkfka - 1):
        if time[j] > time[j + 1]:
            time[j], time[j + 1] = time[j + 1], time[j]

num = 0
total = 0

for k in time:
    num += k
    total += num

print(total)