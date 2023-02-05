# exponent function using conventional for loop

def raise_to_power_function(base_num , power_num):
    final_num = 1
    for num in range(power_num):
        final_num *= base_num
    # print(final_num)
    return final_num

print(raise_to_power_function(2 , 5))


