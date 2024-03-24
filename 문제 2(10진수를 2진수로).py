print("10진수를 2진수로 바꾸는 함수 만들기")
print()
print("예:dec2bin()")

def dec2bin(dec_n):
    sum=0
    i=0
    n=dec_n
    while (n>0):
        remainder =n % 2
        n = n // 2
        sum =sum+(10**i)* remainder
        i=i+1
    return sum

