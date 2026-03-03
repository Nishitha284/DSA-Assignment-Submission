n = int(input("Enter a number: "))
arr = list(map(int, input().split()))

current = 0
maximum = 0

for num in arr:
    if num % 3 == 0:
        current += 1
        if current > maximum:
            maximum = current
    else:
        current = 0

print(maximum)