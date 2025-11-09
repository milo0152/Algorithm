rkrur = int(input())
wksehs = 1000 - rkrur 

rjtmfma = [500, 100, 50, 10, 5, 1] 


num = 0
for i in rjtmfma:
    num += wksehs // i
    wksehs %= i 

print(num)