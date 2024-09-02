str1 = "AbcDEfghIJ"
print(str1.upper())

print(str1.lower())
str2 = " Silver Spoon "
abc = "     welcome to home                "
print(str2.strip())
print(abc.strip())

str3 = "Hello ......"
print(str3.rstrip("."))

str4 = "Silver Spoon"
print(str4.replace("Sp", "M"))

str5 = "Silver Spoon"
print(str5.split(" "))

print(abc.capitalize())

result = abc.strip().capitalize()
print(result)

str6 = "Welcome to the Console!!!"
print(str6.center(50))
print(str6.center(50, "*"))

str7 = "Abracafegdfgdthfncgvjg"
countStr = str7.count("a")
print(countStr)

print(str6.endswith("!!!"))
print(str6.endswith("to", 2, 8))
print(str6.endswith("to", 4, 10))

str8 = "He's name is Dan. He is an honest man."
print(str8.find("is"))
print(str8.find("Daniel"))

print(str8.index("Dan"))
print(str8.index("man"))
# print(str8.index("Daniel"))

str9 = "WelcomeToTheConsole"
print(str9.isalnum())

print(str7.isalpha())

print(abc.islower())

print(str6.isprintable())

xyz = "        "  #using Spacebar"

print(abc.isspace())
print(xyz.isspace())

print(str5.istitle())
print(str8.istitle())

str10 = "WORLD HEALTH ORGANIZATION"
print(str10.isupper())
print(str8.isupper())

print(str6.startswith("Welcome"))
print(str10.startswith("Hello"))

print(str10.swapcase())
print(str9.swapcase())

print(str8.title())
