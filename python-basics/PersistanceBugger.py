def persistence(n):
    temp_num = 1;
    if n <= 9:
        return 0
    else:
        while len(str(n)) > 1:
            for x in str(n):
                temp_num *= int(x)
            n = temp_num
            temp_num = 1
            print("n => " +str(n))

    return n

print(persistence(39))