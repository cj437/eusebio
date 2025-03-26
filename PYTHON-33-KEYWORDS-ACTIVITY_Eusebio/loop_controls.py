def demonstrate_loops():
    for i in range(5):
        if i == 2:
            continue 
        if i == 4:
            break    
        print(i)


    count = 0
    while count < 3:
        print(count)
        count += 1
