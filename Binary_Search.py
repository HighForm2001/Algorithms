import tester


# Need to use a sorted array to search an element from an array.
# in general case.
# in some special case it does not require a sorted array.
# for example, finding an element that is lesser to the element to its left and right
# or finding an element that is bigger to the element to its left and right

def process(arr, target, left, right):
    if left > right:
        return -1
    mid = left + ((right - left) >> 1)
    if arr[mid] < target:
        return process(arr, target, mid + 1, right)
    elif arr[mid] > target:
        return process(arr, target, left, mid - 1)
    else:
        return target


def main():
    arr = tester.random_number_generator(10, 10)
    arr = sorted(arr)
    answer = process(arr, 5, 0, len(arr) - 1)
    print(answer)


if __name__ == "__main__":
    main()
