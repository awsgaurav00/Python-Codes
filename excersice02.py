
start = 2000
end = 4000
result = []
for num in range(start, end + 1):
    if num % 7 == 0 and num % 5 != 0:
        result.append(num)
print(result)