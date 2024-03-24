n = int(input("자연수 n을 입력하세요: "))

era = [True] * n

for i in range(2, n):
    if era[i] == True:
        print(i, end=" ")
        for j in range(i+i, n, i):
            era[j] = False
