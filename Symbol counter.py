print("Привіт!")
text = input("Введіть будь-який текст: ")

text_list = list(text)
result = dict()

for letter in text_list:
    count = 0
    for let in text_list:
        if letter == let:
            count += 1
    result[letter] = count

for key, value in result.items():
    print(f"Символ '{key}' зустрічається {value} разів")

