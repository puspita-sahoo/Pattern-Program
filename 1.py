rows = 4

for i in range(1,rows+1):
    num = i
    for j in range(i):
        print(num, end='')
        num += 1
    print()