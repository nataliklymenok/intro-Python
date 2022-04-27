print("Привіт!")
input1 = int(input("Введіть перше ціле число: "))
operation = str(input("Введіть одну з операцій: +, -, *, /, +++: "))

if operation in ("+", "-", "*", "/", "+++"):
    input2 = int(input("Введіть друге ціле число: "))
    
    if operation == "+":
        result = input1 + input2
    elif operation == "-":
        result = input1 - input2
    elif operation == "*":
        result = input1 * input2
    elif operation == "/":
        try:
            result = input1 / input2
        except ZeroDivisionError:
            print("На 0 ділити неможна!")
            result = "inf"
    elif operation == "+++":
        result = input1 + input2
        while input2 != "":
            input2 = input("Введіть наступне ціле число: ")
            if input2.isdigit():
                result += int(input2)
    print(f"Результат: {str(result)}")
   
else:
    print("Помилка! Невірна операція!")
