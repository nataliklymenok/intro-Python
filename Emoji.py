print("Привіт!")
print("Введіть будь-яку фразу зі смайлами :), XD, :(, >:(, >:) :")
input1 = input()
smile = ":)" 
lol = "XD"
sad = ":("
mad = ">:(" 
devil = ">:)"
emoji = input1.replace(mad, "😠").replace(devil, "😈").replace(smile, "🙂").replace(lol, "😂").replace(sad, "🙁")
print(emoji)
