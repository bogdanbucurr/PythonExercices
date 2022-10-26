'''

The included code stub will read an integer, n, from user.
Without using any string methods, try to print the following:

'123...n'

Note that '...' represents the consecutive values in between

'''

if __name__ == '__main__':
    print('Hi there your row will start with 1 you should now that\n',
          'Please insert your last number from your row here: ')
    n = int(input())

    for i in range(1, n+1):
        print(i, end='')