import tester
def process(arr):
    if not arr or len(arr) < 2:
        return
    for x in range(0, len(arr)):
        min_index = x
        for y in range(x+1, len(arr)):
            min_index = y if arr[y] < arr[min_index] else min_index
        swap(arr,x,min_index)

def swap(arr, n_1, n_2):
    temp = arr[n_1]
    arr[n_1] = arr[n_2]
    arr[n_2] = temp

if __name__ == "__main__":
    test = tester.random_number_generator(100,10)
    print(test)
    test_2 = test.copy()
    process(test)
    test_2.sort()
    print(test)
    print(test_2)