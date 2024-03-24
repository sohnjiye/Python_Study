print("16진수를 10진수로 바꾸는 함수 만들기" )
print()
print("예 :hec2dec('A1A1')   (*대문자와 작은따옴표를 함께 입력하세요)")

def hec2dec(hec_n):
    hec_str = str(hec_n)
    hec_n = list(hec_str)
    hec_n.reverse()
    Sum = 0
    i=0
    size=len(hec_str)

    while size>0 :

        if int(hec_n[i] == 'A'):
            hec_n[i] = 10

        elif int(hec_n[i] == 'B'):
            hec_n[i] = 11

        elif int(hec_n[i] == 'C'):
            hec_n[i] = 12

        elif int(hec_n[i] == 'D'):
            hec_n[i] = 13

        elif int(hec_n[i] == 'E'):
            hec_n[i] = 14

        elif int(hec_n[i] == 'F'):
            hec_n[i] = 15

            i=i+1
            size=size-1

        else:

            hec_n[i] = hec_n[i]

        Sum = Sum + (int(hec_n[i]) * (16 ** i))
        i=i+1
        size=size-1

    return (Sum)

