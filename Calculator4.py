
def isNumber(question):
    inp = input(question)

    if isInt(inp):
        return int(inp)
    elif isFloat(inp):
        return float(inp)
    else:
        print("Помилка!")
        isNumber(question)


def isInt(inp):
    try:
        int(inp)
        return True
    except ValueError:
        return False

def isFloat(inp):
    try:
        float(inp)
        return True
    except ValueError:
        return False


print("Привіт!")
input1 = isNumber("Введіть перше число: ")
operation = input("Введіть одну з операцій: +, -, *, /, +++: ")

if operation in ("+", "-", "*", "/", "+++"):
    input2 = isNumber("Введіть друге число: ")

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
            input2 = isNumber("Введіть наступне число: ")
            result += input2
    print(f"Результат: {str(result)}")

else:
    print("Помилка! Невірна операція!")




#1. Тепер користувач має мати можливість вводити будь-які числа, а не тільки цілі (тобто 3.5, 0.001, -25.3 - також мають підходити)

#2. Зробити функцію яка запитує у користувача число та перевіряє чи це дійно число.
#Якщо ні - виводить помилку та запитує ще раз. Використати цю функцію для запиту числа в користувача.