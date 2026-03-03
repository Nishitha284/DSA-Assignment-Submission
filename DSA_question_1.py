# Problem 1: Find All Multiples of 36

n = int(input("Enter a number: "))
arr = list(map(int, input().split()))
result = []

for num in arr:
    if num % 3 == 0:
        result.append(num)
if len(result) == 0:
    print(-1)
else: print(result)

