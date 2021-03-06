class Calculator:
    def __init__(self, _operation, _operand1, *_operand2):
        self.operation = _operation
        self.operand1 = _operand1
        self.operand2 = _operand2

    def add(self, a, b):
        return a + b[0]

    def sub(self, a, b):
        return a - b[0]

    def mul(self, a, b):
        return a * b[0]

    def div(self, a, b):
        try:
            divisio = a / b[0]
        except ZeroDivisionError:
            print("На 0 ділити неможна!")
            divisio = "inf"
        return divisio

    def add_mul(self, a, b):
        _result = a
        for element in b:
            _result += element
        return _result

    OPERATIONS = {
        '+': add,
        '-': sub,
        '/': div,
        '*': mul,
        '+++': add_mul,
    }

    def calculate(self, _operation, a, b):
        global result
        if _operation in self.OPERATIONS.keys():
            result = self.OPERATIONS[_operation](self, a, b)
        else:
            print("Помилка! Невірна операція!")
            exit()

        return result

    def print_result(self, _result):
        if self.operation in ('+', '-', '*', '/'):
            print(f"{self.operand1} {self.operation} {self.operand2[0][0]} = {_result}")
        else:
            pretty_string = (' + '.join([str(a) for a in self.operand2[0]]))
            print(f"{self.operand1} + {pretty_string} = {_result}")


class Verifier:

    @staticmethod
    def is_operation_common(inp):
        if inp in ("+", "-", "*", "/"):
            return True
        else:
            return False

    @staticmethod
    def is_operation_difficult(inp):
        if inp == "+++":
            return True
        else:
            return False

    @staticmethod
    def is_float(inp):
        try:
            float(inp)
            return True
        except ValueError:
            return False


class Creator:
    operand1 = None
    operand2 = None

    @staticmethod
    def create_first_operand():
        global operand1
        is_number = False
        while not is_number:
            operand1 = input("Введіть перше число: ")
            is_number = Verifier.is_float(operand1)
        return float(operand1)

    @staticmethod
    def create_second_operand():
        global operand2
        is_number = False
        while not is_number:
            operand2 = input("Введіть друге число: ")
            is_number = Verifier.is_float(operand2)
        return [float(operand2)]

    @staticmethod
    def create_multi_operand():
        is_number = True
        _operand2 = []
        while is_number:
            input_val = input("Введіть наступне число: ")
            if input_val != '':
                if not Verifier.is_float(input_val):
                    continue
                _operand2.append(float(input_val))
            else:
                is_number = False
        return _operand2


if __name__ == '__main__':
    operand1 = None
    operand2 = None

    operation = input("Введіть одну з операцій: +, -, *, /, +++: ")

    if Verifier.is_operation_common(operation):
        operand1 = Creator.create_first_operand()
        operand2 = Creator.create_second_operand()

    elif Verifier.is_operation_difficult(operation):
        operand1 = Creator.create_first_operand()
        operand2 = Creator.create_multi_operand()

    calc = Calculator(operation, operand1, operand2)
    result = calc.calculate(operation, operand1, operand2)
    calc.print_result(result)
