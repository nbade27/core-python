try:
    num = 10/0
    number = int(input("Enter number "))
    print(number)
except ZeroDivisionError as err:
    # print("We cannot divide with 0")
    print(err)
except ValueError:
    print("Invalid input you should enter integer!!!")