from math import *


def narcissistic(value):
    given_number = value
    power_number = 0
    number_list = []
    final_number = 0
    print(value % 10)
    if len(str(value)) <= 1:
        power_number = 1
        number_list.append(value % 10)
    else:
        while value > 0:
            # print("String value " + str(value))
            number_list.append(value % 10)
            power_number = power_number + 1
            value -= value % 10
            value = ceil(value / 10)

    print(power_number)
    for x in number_list:
        final_number += pow(x, power_number)

    if int(final_number) == given_number:
        result = True
    else:
        result = False


    return result

print(narcissistic(370))

#
# from math import *
#
#
# def narcissistic(value):
#     return value == sum(int(x) ** len(str(value)) for x in str(value))
#
#
# print(narcissistic(371))