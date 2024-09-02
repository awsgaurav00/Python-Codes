#Example 1
print(15+9)
print(25-3)
print(9*5)
print(60/3)
print(45%2)
print(6**8)
print(400//2)


#Example 2
n = float(input("Enter the First Number: "))
m = float(input("Enter the Second Number: "))

#addition

print("{} + {} = ".format(n, m))
print(n + m)

#subtraction

print("{} - {} = ".format(n, m))
print(n - m)

#multiplication

print("{} * {} = ".format(n, m))
print(n - m)

#division

print("{} / {} = ".format(n, m))
print(n / m)


#Example 3
x = float(input("Enter the Values of x: "))
y = float(input("Enter the Values of y: "))

ans1 = x + y
print("Addition of", x, "and", y, "is", ans1)

ans2 = x - y
print("subtration of", x, "and", y, "is", ans2)

ans3 = x * y
print("multiplication of", x, "and", y, "is", ans3)

ans4 = x / y
print("division of", x, "and", y, "is", ans4)

ans5 = x // y
print("floor division of", x, "and", y, "is", ans5)

ans6 = x**y
print("Expoential of", x, "and", y, "is", ans6)

ans7 = x % y
print("modulos of", x, "and", y, "is", ans7)
