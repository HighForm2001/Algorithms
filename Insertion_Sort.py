import tester


def process(arr):
    if not arr or len(arr) < 2:
        return
    for x in range(1, len(arr)):
        j = x - 1
        while j >= 0 and arr[j] > arr[j + 1]:
            swap(arr, j, j + 1)
            j -= 1


def swap(arr, x, y):
    temp = arr[x]
    arr[x] = arr[y]
    arr[y] = temp


if __name__ == "__main__":
    test = tester.random_number_generator(100, 25)
    test_2 = test.copy()
    print(test)
    process(test)
    test_2.sort()
    print(test)
    print(test_2)
