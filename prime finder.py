
for i in range(1, 1000):
    j = i - 1
    x = 0
    while(j > 1):
        if i % j == 0:
            x = -1
            j = -1
        j -= 1
    if x != -1:
        print(str(i) + " is prime\n")
