# def print_every_other(low, high):
#     if low > high:
#         return
#     print(low)
#     print_every_other(low + 2, high)
#
#
# print_every_other(0, 12)


# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 2)
#
# print(factorial(4))

# def summ(low, high):
#     if low > high:
#         return 0
#     return low + summ(low + 1, high)
#
# print(summ(1, 100))


def print_only_digits(arr):
    for i in arr:
        if type(i) == list:
            print_only_digits(i)
        else:
            print(i)


array = [1, 2, 3, [4, 5, 6], 7, [8, [9, 10, 11], 12], 13]

print_only_digits(array)
