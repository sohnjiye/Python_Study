# 10진수 -> 2진수
a=[]
def dec2bin(n):
        a=[]
        while n>=1:
            if n%2==0:
                a.append('0')
            else:
                a.append('1')
            n//=2
        a.reverse()
        for i in a:
            print(i, end='')

# 16진수 -> 10진수
def hex2dec(num):
    str_num = str(num)

    num = list(str_num)

    num.reverse()

    sum_n = 0

    for i in range(0, len(str_num)):

        if int(num[i] == 'A'):

            num[i] = 10

        elif int(num[i] == 'B'):

            num[i] = 11

        elif int(num[i] == 'C'):

            num[i] = 12

        elif int(num[i] == 'D'):

            num[i] = 13

        elif int(num[i] == 'E'):

            num[i] = 14

        elif int(num[i] == 'F'):

            num[i] = 15

        else:

            num[i] = num[i]

        sum_n = sum_n + (int(num[i]) * (16 ** i))

    return (sum_n)

