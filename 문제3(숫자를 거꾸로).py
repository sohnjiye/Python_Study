print("숫자를 입력하면 뒤집어서 출력하는 함수")
print()
print("예: reverse()")
def reverse(temp):
    r=0
  
    while temp!=0:
        remainder=temp%10
        temp=temp//10
        r=r*10+remainder
    return r    


