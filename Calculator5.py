class Calculator:
    def __init__(self, operation, operand1, *operand2):
        self.operation = operation
        self.operand1 = operand1
        self.operand2 = operand2


    def summ(self):
        return self.operand1 + self.operand2[0]


    def subtr(self):
        return self.operand1 - self.operand2[0]


    def mult(self):
        return self.operand1 * self.operand2[0]


    def divis(self):
        try:
            divisio = self.operand1 / self.operand2[0]
        except ZeroDivisionError:
            print("На 0 ділити неможна!")
            divisio = "inf"
        return divisio



    def calculate(self):
        result = None
        if self.operation == "+":
            result = self.summ()

        elif self.operation == "-":
            result = self.subtr()

        elif self.operation == "*":
            result = self.mult()

        elif self.operation == "/":
            result = self.divis()


        elif self.operation == "+++":
            result = self.operand1
            for element in self.operand2[0]:
                result += element

        else:
            print("Помилка! Невірна операція!")
            exit()

        return result


    def printResult(self, result):
        if self.operation in ('+', '-', '*', '/'):
            print(f"{self.operand1} {self.operation} {self.operand2[0]} = {result}")
        else:
            prettyString = (' + '.join([str(a) for a in self.operand2[0]]))
            print(f"{self.operand1} + {prettyString} = {result}")


class Verifier:


    def isOperationCommon(self, inp):
        if inp in ("+", "-", "*", "/"):
            return True
        else:
            return False


    def isOperationDifficult(self, inp):
        if inp == "+++":
            return True
        else:
            return False


    def isFloat(self, inp):
        try:
            float(inp)
            return True
        except ValueError:
            return False


if __name__ == '__main__':
    verifier = Verifier()
    operand1 = None
    operand2 = []

    operation = input("Введіть одну з операцій: +, -, *, /, +++: ")

    if verifier.isOperationCommon(operation):

        isNumber = False
        while not isNumber:
            operand1 = input("Введіть перше число: ")
            isNumber = verifier.isFloat(operand1)
        operand1 = float(operand1)

        isNumber = False
        while not isNumber:
            operand2 = input("Введіть друге число: ")
            isNumber = verifier.isFloat(operand2)
        operand2 = float(operand2)

    elif verifier.isOperationDifficult(operation):

        isNumber = False
        while not isNumber:
            operand1 = input("Введіть перше число: ")
            isNumber = verifier.isFloat(operand1)
        operand1 = float(operand1)

        isNumber = True
        while isNumber:
            inputVal = input("Введіть наступне число: ")
            if inputVal != '':
                if not verifier.isFloat(inputVal):
                    continue
                operand2.append(float(inputVal))
            else:
                isNumber = False

    calc = Calculator(operation, operand1, operand2)
    result = calc.calculate()
    calc.printResult(result)
