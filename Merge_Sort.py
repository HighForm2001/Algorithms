def main():
    arr = [1, 3, 5, 2, 4, 8, 0]

    sorted_array = process(arr, 0, len(arr) - 1)
    print(sorted_array)


def process(arr, left: int, right: int):
    if left == right:
        return [arr[left]]
    mid = left + ((right - left) >> 1)
    left_array = process(arr, left, mid)
    right_array = process(arr, mid + 1, right)
    return merge(left_array, right_array)


def merge(arr1, arr2):
    res = []
    left_pointer, right_pointer = 0, 0
    while (left_pointer < len(arr1) and right_pointer < len(arr2)):
        if (arr1[left_pointer] <= arr2[right_pointer]):
            res.append(arr1[left_pointer])
            left_pointer += 1
        else:
            res.append(arr2[right_pointer])
            right_pointer += 1
    while (left_pointer < len(arr1)):
        res.append(arr1[left_pointer])
        left_pointer += 1
    while (right_pointer < len(arr2)):
        res.append(arr2[right_pointer])
        right_pointer += 1
    return res

if __name__ == "__main__":
    main()