import timeit
print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=100000))
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=100000))