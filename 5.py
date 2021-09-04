start = 1
stop = 2
num = stop      #num = 2
for i in range(2, 6):    #row = 4=3
    for j in range(start, stop):      #col=3    ,start=4    ,stop=7
        num -= 1         #num = 4
        print(num, end='')
    print("")
    start = stop        #start = 4
    stop += i         #stop = 7
    num = stop   #num = 7
