print("Привіт!")
print("Введіть будь-яку фразу зі словом cucumber:")
input1 = input()
cucumber = "cucumber"

if cucumber in input1:
    index_start = input1.find(cucumber)
    index_end = index_start + len(cucumber)
    print(input1[index_end:])
else:
    print("Шкода :( слово cucubmer не знайдено")
