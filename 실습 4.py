# 실습 4
p = int(input("원금: "))
i = float(input("이자율: ")) / 12
n = int(input("상환횟수: ")) * 12
month = p * (i * (1 + i)**n) / ((1 + i)**n - 1)
print("월 상환액은", month, "입니다")
