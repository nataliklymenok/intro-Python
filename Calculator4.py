def number(question, isRepeatedly=False):
    inp = input(question)

    if isInt(inp):
        return int(inp)
    elif isFloat(inp):
        return float(inp)
    elif isRepeatedly:
        if inp == "":
            return None
        else:
            print("Помилка!")
            return number(question, True)
    else:
        print("Помилка!")
        return number(question)


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
input1 = number("Введіть перше число: ")
operation = input("Введіть одну з операцій: +, -, *, /, +++: ")

if operation in ("+", "-", "*", "/", "+++"):
    input2 = number("Введіть друге число: ")

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
        while True:
            input2 = number("Введіть наступне число: ", True)
            if input2 != None:
                result += input2
            else:
                break
    print(f"Результат: {result}")

else:
    print("Помилка! Невірна операція!")
