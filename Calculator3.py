print("Привіт!")
print("Введіть перше ціле число:")
input1 = input()
print("Введіть одну з операцій: +, -, *, /, +++:")
operation = str(input())

if operation in ("+", "-", "*", "/", "+++"):
    print("Введіть друге ціле число:")
    input2 = input()
    
    if operation == "+":
        result = int(input1) + int(input2)
    elif operation == "-":
        result = int(input1) - int(input2)
    elif operation == "*":
        result = int(input1) * int(input2)
    elif operation == "/":
        try:
            result = int(input1) / int(input2)
        except ZeroDivisionError:
            print("На 0 ділити неможна!")
            result = "inf"
    elif operation == "+++":
        result = int(input1) + int(input2)
        while input2 != "":
            print("Введіть наступне ціле число:")
            input2 = input()
            if input2.isdigit():
                result += int(input2)
    print("Результат: " + str(result))
   
else:
    print("Помилка! Невірна операція!")
