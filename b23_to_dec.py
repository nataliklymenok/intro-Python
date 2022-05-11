print("Ласкаво просимо у конвертер системи числення з базою 23 в десяткову :)")
print("Допустимі символи та їх значення:")

b23 = {"0": "0", "1": "1", "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9": "9", "A": "10",
       "B": "11", "C": "12", "D": "13", "E": "14", "F": "15", "G": "16", "H": "17", "I": "18", "J": "19", "K": "20",
       "L": "21", "M": "22", }

for key, value in b23.items():
    print(f"{key} = {value}")

inp_list = list(input("Введіть число в базі 23: "))

inp_list.reverse()
dec = 0
new_list = list()

for element in inp_list:
    if element in b23.keys():
        new_list.append(b23[element])
    else:
        print("Введене число не відповідає базі")
        exit()

for index, element in enumerate(new_list):
    dec += int(element) * 23 ** index

print("Ваше число в десятковій системі числення: ", dec)
