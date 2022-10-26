'''

Given a time in 12 hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

'''
import os


def timeConversion(s):
    unit = s[-2:]

    first_two = int(s[:2])
    remaining = s[2:len(s) - 2]
    if unit == "PM" and first_two < 12:
        convert = str(12 + first_two)
        return convert + remaining
    elif unit == "AM" and first_two == 12:
        return "00" + remaining
    else:
        return s[:len(s) - 2]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()


    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
