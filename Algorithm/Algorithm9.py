num = int(input())

rkfh = 1
tpfh = 0

for i in range(10000000):
    if num > (i + 1):
        num -= (i + 1)
        rkfh += 1
    else:
        line = rkfh
        tpfh = num

        if line % 2 == 0:
            wk = tpfh
            ah = line - tpfh + 1
        else:
            wk = line - tpfh + 1
            ah = tpfh

        print(f"{wk}/{ah}")
        break
