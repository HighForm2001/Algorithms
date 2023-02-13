def heapSort(arr):
    if not arr or arr.length < 2:
        return
    for i in range(0,len(arr)):
        heapInsert(arr,i)  # 构建大根堆 O(logN)
    heapSize = arr.length
    swap(arr,0,heapSize-1)
    heapSize-=1
    while(heapSize>0):
        heapify(arr, 0, heapSize) # O(logN)
        heapSize -=1
        swap(arr, 0, heapSize) # O(1)
def heapify(arr, index, heapsize):
    left = 2*index+1 # check if has kid
    while(left < heapsize): # if left < heapsize, means has kid
        largest = left+1 if (left + 1 < heapsize and arr[left+1] > arr[left]) else left
        largest = largest if arr[largest] > arr[index] else index # index = father
        if (largest == index):
            break
        swap(arr, largest, index) # for example, largest = 3, index = 1, largest win
        # if index win, largest = index, so break
        index = largest # index = 3, left = 2 * 3 + 1
        left = 2 * index + 1

def heapInsert(arr, index):
    while(arr[index] > arr[(index-1)/2]):
        swap(arr,index, (index-1)/2)
        index = (index-1)/2

def swap(arr, index1, index2):
    temp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = temp

