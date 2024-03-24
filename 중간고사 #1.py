a, b, c = 0, 0, 0
result = 0

select = input("1. 수식계산기 2. 두수 사이 합계: ")

if select == '1':
    a = input("*** 수식을 입력하세요: ")
    print("%s 결과는  %0.1f 입니다." %(a, eval(a)))

elif select == '2':
    b = int(input("첫 번째 숫자를 입력하세요: "))
    c = int(input("두 번째 숫자를 입력하세요: "))

    for i in range(b,c+1):
        result = result + i

    print("%d+...+%d는 %d입니다." %(b, c, result))

else:
    print("1 또는 2만 입력해야합니다.")
