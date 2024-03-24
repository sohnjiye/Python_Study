import random

number = []
for num in range(0, 10):
    number.append(random.randrange(0, 10))


print("생성된 리스트", number)

for num in range(0, 10):
    if num not in number:
        print(num, "숫자는 리스트에 없네요.")
