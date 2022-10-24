'''

Ex. 1

Given an array of integers, calculate the ratios of its elements that are positive,
negative, and zero. Print the decimal value of each fraction on a new line with 6 places
after the decimal.

'''


def plusMinus(arr):
    positive = len([i for i in arr if i > 0]) / len(arr)

    negative = len([i for i in arr if i < 0]) / len(arr)
    zero = len([i for i in arr if i == 0]) / len(arr)
    print("{:.6f}\n{:.6f}\n{:.6f}".format(positive, negative, zero))


if __name__ == '__main__':
    print("Enter de 'n' value (the length of the list): ")

    n = int(input().strip())

    print("Enter your array without any '[]' or ',' between the numbers: ")
    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

