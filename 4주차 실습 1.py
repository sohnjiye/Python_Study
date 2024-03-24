passwd = 1234
init = "Y"
a = int(input("비밀번호를 입력하세요: "))
if passwd == a:
    print("상자가 열렸습니다. 보물 획득")
else:
    print("비밀번호가 틀렸습니다.")
    b = input("비밀번호를 초기화하시겠습니까? Y/N")
    if init == b:
            passwd = int(input("비밀번호를 다시 설정하세요: "))
            c = int(input("비밀번호를 입력하세요: "))

            if passwd == c:
                print("상자가 열렸습니다. 보물 획득")

            else:
                print("비밀번호가 틀렸습니다.")

    else:
            print("비밀번호를 초기화하지 않았습니다")
