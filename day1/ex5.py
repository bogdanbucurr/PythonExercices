'''

Ms. Gabriel Williams is a botany professor at District College. One day, she asked her
student Mickey to compute the average of all the plants with distinct heights in her greenhouse.

Formula used: average=sum of distinct height/total number of distinct heights

'''


def average(array):
    l = set(arr)
    return (sum(l) / len(l))


if __name__ == '__main__':
    # print('Please let us know the total number of distinct heights: ')
    # n = int(input())
    print('Please insert the heights: ')
    arr = list(map(int, input().split(',')))
    result = average(arr)
    print(result)
