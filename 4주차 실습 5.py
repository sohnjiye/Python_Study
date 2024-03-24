print("i부터 n 까지의 합을 계산하면 얼마일까요?")
i = int(input("연산할 시작 수를 입력하세요: "))
n = int(input("연산할 마지막 수를 입력하세요: "))
result = 0

while i <= n:
    result = result + i
    i = i + 1

print("합은", result, "입니다")
