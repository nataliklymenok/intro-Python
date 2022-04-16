print("Привіт!")
print("Введіть перше число:")
input1 = input()
print("Введіть друге число:")
input2 = input()
if int(input1) > int(input2):
    print("Перше число більше ніж друге число")
elif int(input1) < int(input2):
    print("Перше число менше ніж друге число")
else:
    print("Числа дорівнюють один одному")
    