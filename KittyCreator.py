import argparse
import os
import random
import requests as requests

parser = argparse.ArgumentParser(description='Створювач кицьок :3')
parser.add_argument(
    'amount',
    type=int,
    help='Кількість картинок з кицьками'
)
parser.add_argument(
    'out_dir',
    type=str,
    nargs='?',
    const=True,
    default=False,
    help='Директорія для збереження картинок'
)
parser.add_argument(
    '--gray',
    dest='gray',
    nargs='?',
    const=True,
    default=False,
    help='Створити чорно-білих кицьок'
)

args = parser.parse_args()
pathToRepo = os.getcwd()


def createCat(count, out_dir=False, isGray=False):
    if not out_dir:
        out_dir = ''
    path = os.path.join(pathToRepo, out_dir)

    if not os.path.exists(path):
        os.mkdir(path)

    print(f"Вітаю! Зараз будемо створбвати кицьок :3 в папці {path}")

    for n in range(1, count + 1):
        print(f"Створюємо {n} кицьку")
        url = f'http://placekitten.com/{random.randint(100, 1000)}/{random.randint(100, 1000)}'
        if isGray:
            url = f'http://placekitten.com/g/{random.randint(100, 1000)}/{random.randint(100, 1000)}'
        respond = requests.post(url)
        with open(f"{path}/cat{n}.jpg", "wb") as file:
            file.write(respond.content)


createCat(args.amount, args.out_dir, args.gray)
