import random
import tester


def main():
    arr = tester.random_number_generator(300, 100)
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)


def swap(arr, index1, index2):
    temp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = temp
    # arr[index1] = arr[index1] ^ arr[index2]
    # arr[index2] = arr[index1] ^ arr[index2]
    # arr[index1] = arr[index1] ^ arr[index2]


def quick_sort(arr, L, R):
    if L < R:
        swap(arr, L + random.randint(0, R - L), R)
        p = partition(arr, L, R)
        quick_sort(arr, L, p[0] - 1)
        quick_sort(arr, p[1] + 1, R)


def partition(arr, L, R):
    less = L - 1  # left boundary
    more = R  # right boundary
    while (L < more):
        if arr[L] < arr[R]:
            # move boundary first
            less += 1
            # swap
            swap(arr, less, L)
            L += 1
        elif arr[L] > arr[R]:
            # move boundary first
            more -= 1
            swap(arr, more, L)
        else:
            L += 1
    swap(arr, more, R)
    return less + 1, more


if __name__ == "__main__":
    main()
