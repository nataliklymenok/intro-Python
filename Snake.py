import random
import time

print("Привіт! Зараз будет змійка о_О")
r = random.randint(5, 50)
whitespace = " "

while True:
    try:
        time.sleep(0.1)
        print(f"{whitespace * r} *")
        r = random.randint(r - 1, r + 1)
    except KeyboardInterrupt:
        print(f"{whitespace * r} o_O")
        exit()
