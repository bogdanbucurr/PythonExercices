'''

Given five positive integers, find the minimum and maximum values that can be calculated by
summing exactly four of the five integers. Then print the respective minimum and maximum values
as a single line of two space-separated long integers.

'''


def miniMaxSum(arr):
    arrMin = arr.copy()
    arrMax = arr.copy()
    minVal = 0
    maxVal = 0

    i = 0
    while len(arrMin) > 1:
        if arrMin[i] <= arrMin[i + 1]:
            minVal += arrMin.pop(i)
        else:
            minVal += arrMin.pop(i + 1)


    j = 0
    while len(arrMax) > 1:
        if arrMax[j] >= arrMax[j + 1]:
            maxVal += arrMax.pop(j)
        else:
            maxVal += arrMax.pop(j + 1)

    print(minVal, maxVal)


if __name__ == '__main__':

    print("Enter the numbers without any '[]' or ',' between them: ")
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
