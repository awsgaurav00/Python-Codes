#elif statement

num = int(input("Enter the number: "))
print("The number is: ", num)

if (num < 0):
  print("Number is negative.")
elif (num == 0):
  print("Number is Zero.")
else:
  print("Number is positive.")
