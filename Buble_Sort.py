import tester

def process(arr):
    if not arr or len(arr) < 2:
        return
    for x in range(len(arr)-1,0,-1):
        y = 0
        while y < x:
            if arr[y] > arr[y+1]:
                swap(arr,y,y+1)
            y += 1
def swap(arr, x, y):
    temp = arr[x]
    arr[x] = arr[y]
    arr[y] = temp

if __name__ == "__main__":
    test = tester.random_number_generator(100,20)
    test_2 = test.copy()
    print(test)
    process(test)
    test_2.sort()
    print(test)
    print(test_2)