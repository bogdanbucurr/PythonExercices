'''

Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
You are given 'n' scores. Store them in a list and find the score of the runner-up.

'''

if __name__ == '__main__':

    print('Enter your inputs, please:')
    #n = int(input())
    arr = map(int, input().split())

    # creating a list
    l = list(arr)

    # sorting list
    l1 = sorted(l)

    # using set() method to remove duplicated numbers
    set1 = set(l1)

    # making list from set to be able to get number from index
    l2 = list(set1)

    # getting runner up score from index
    print(l2[-2])
