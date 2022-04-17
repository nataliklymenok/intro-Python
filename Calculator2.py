print("Привіт!")
print("Введіть перше ціле число:")
input1 = input()
print("Введіть одну з операцій: +, -, *, /:")
operation = str(input())

if operation in ("+", "-", "*", "/"):    
    print("Введіть друге ціле число:")
    input2 = input()
    
    if operation == "+":
        result = str(int(input1) + int(input2))
    if operation == "-":
        result = str(int(input1) - int(input2))
    if operation == "*":
        result = str(int(input1) * int(input2))
    if operation == "/":
        result = str(int(input1) / int(input2))            
    print("Результат: " + result)
else:
    print("Помилка! Невірна операція!")
    



