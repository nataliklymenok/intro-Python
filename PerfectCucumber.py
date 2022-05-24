def input_perfect_cucumner():
    cucumber = input("Введи слово Сucumber: ")
    assert cucumber[:1].isupper(), "Слово повинно писатися з великої літери, а у тебе з маленької!"
    assert cucumber[1:].islower(), "Не всі літери, окрім першої, маленькі!"
    assert ' ' not in cucumber, "Введене слово містить зайві пробіли!"
    assert cucumber == "Cucumber", "Ти ввів не Cucumber =/"
    return cucumber


print("Привіт! Тобі випала честь врятувати грецький салат 🍅🫑🫒🧀 і знайти правильний Cucumber! "
      "Давай зробимо це швидко та без помилок? :)")
question = None
while question is None:
    try:
        question = input_perfect_cucumner()
        print("Ну нарешті! Дякую 🥗")
    except AssertionError as error:
        print(error)
    except KeyboardInterrupt:
        print("Ех, здався :(((")
        break
