coffee = 0

def coffee_machine(button):

    print()
    print("#1. (자동으로) 뜨거운 물을 준비한다.")
    print("#2. (자동으로) 종이컵을 준비한다.")

    if button  == 1:
        print("#3. (자동으로) 보통커피를 탄다")

    elif button  == 2:
        print("#3. (자동으로) 설탕커피를 탄다")

    elif button  == 3:
        print("#3. (자동으로) 블랙커피를 탄다")

    else:
        print()

    print("#4. (자동으로) 물을 붓는다")
    print("#5. (자동으로) 스푼으로 저어서 녹인다")
    print()
    print("손님~ 커피 여기 있습니다.")

coffee = int(input("어떤 커피 드릴까요? (1:보통, 2:설탕, 3:블랙) "))
coffee_machine(coffee)

# 1,2,3 이외의 값의 경우 그냥 공백으로 출력되도록 설정하였습니다.
