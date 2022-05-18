import random

randomList = []
for i in range(0, 10):
    randomList.append(random.randint(0, 100))


def sorter(unsorted_list):
    sorted_list = []
    for index in range(0, len(unsorted_list)):
        min_value = min(unsorted_list)
        sorted_list.append(min_value)
        unsorted_list.remove(min_value)
    return sorted_list


print(f"Initial list: {randomList}")
print(f"Sorted list: {sorter(randomList)}")
