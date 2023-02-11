import random
import Merge_Sort
import Quick_Sort


def random_number_generator(length, random_range):
    res = []
    for x in range(0, length):
        res.append(random.randint(0, random_range))
    return res


def tester():
    for x in range(2):
        tester_1 = random_number_generator(10000, 300)
        tester_2 = tester_1.copy()
        print(tester_1)
        print(tester_2)
        Quick_Sort.quick_sort(tester_1, 0, len(tester_1) - 1)
        tester_2 = sorted(tester_2)
        print(tester_1)
        print(tester_2)


if __name__ == "__main__":
    tester()
