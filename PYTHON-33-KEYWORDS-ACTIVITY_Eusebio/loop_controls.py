def demonstrate_loops():
    for i in range(5):
        if i == 2:
            continue  # Skip 2
        if i == 4:
            break    # Stop at 4
        print(i)

    # while loop
    count = 0
    while count < 3:
        print(count)
        count += 1
