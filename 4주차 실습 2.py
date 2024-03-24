import turtle
t=turtle.Turtle()
i= 0
n=int(input("정수를 입력하세요: "))

while i<n:

    if (n<3 or n>10):
        print("3이상 10이하 정수만 입력하세요")
        n=int(input("정수를 입력하세요: "))

    else:
        degree=360/n
        t.forward(100)
        t.left(degree)
        i=i+1

