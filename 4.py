start = 1
stop = 2
current_num = stop      #current_num = 2
for row in range(2, 6):    #row = 4=3
    for col in range(start, stop):      #col=3    ,start=4    ,stop=7
        current_num -= 1         #current_num = 4
        print(current_num, end='')
    print("")
    start = stop        #start = 4
    stop += row         #stop = 7
    current_num = stop   #current_num = 7
