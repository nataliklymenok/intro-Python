print("Привіт!")
direction = int(input("Введіть 1 якщо хочеш зашифрувати текст, 2 - якщо розшифрувати: "))

while direction != 1 and direction != 2:
    print("Невірний напрямок, спробуй ще раз!")
    direction = int(input("Введіть 1 якщо хочеш зашифрувати текст, 2 - якщо розшифрувати: "))

text = list(input("Введіть текст: "))

try:
    key = int(input("Введіть ключ зсуву - ціле число: "))
except ValueError:
    print("Невірний ключ зсуву! Спробуй спочатку :)")
    exit()

key = abs(key) % 26
new_text = list()

if direction == 1:
    for character in text:
        if character.isalpha() and character.isupper():
            new_order = ord(character) + key
            if new_order > ord("Z"):
                new_order = new_order - ord("Z") + ord("A") - 1
            new_text.append(chr(new_order))
        elif character.isalpha() and character.islower():
            new_order = ord(character) + key
            if new_order > ord("z"):
                new_order = new_order - ord("z") + ord("a") - 1
            new_text.append(chr(new_order))
        else:
            new_text.append(character)

if direction == 2:
    for character in text:
        if character.isalpha() and character.isupper():
            new_order = ord(character) - key
            if new_order < ord("A"):
                new_order = new_order - ord("A") + ord("Z") + 1
            new_text.append(chr(new_order))
        elif character.isalpha() and character.islower():
            new_order = ord(character) - key
            if new_order < ord("a"):
                new_order = new_order - ord("a") + ord("z") + 1
            new_text.append(chr(new_order))
        else:
            new_text.append(character)

print(''.join(new_text))

