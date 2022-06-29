import datetime
import time
from concurrent.futures import ThreadPoolExecutor
import requests as requests

now_sec = datetime.datetime.now().strftime("%S")
listA = [f"{i:0>3}" for i in range(0, 1000)]


def check_code(code):
    response = requests.post('http://code.qqmber.wtf/guess/', json={"password": f"{code}"})

    if response.status_code == requests.codes.ok:
        print(f"Done! Password is {code}")


def execute():
    with ThreadPoolExecutor(max_workers=50) as executor:
        for i in range(0, 1000):
            executor.submit(check_code, listA[i])


if __name__ == '__main__':
    while now_sec != '00':
        remaining = 60 - int(now_sec)
        print(f"Seconds before execution = {remaining}")
        time.sleep(1)
        now_sec = datetime.datetime.now().strftime("%S")

    execute()
