def heapify(arr, n, i):
    largest = i  #假設根節點為最大值，從0開始
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2

    # 如果左邊子節點存在且大於根節點
    if l < n and arr[i] < arr[l]:
        largest = l

    # 如果右邊子節點存在且大於根節點
    if r < n and arr[largest] < arr[r]:
        largest = r

    # 如果最大值不等於i，就做交換
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  #做交換

        # Heapify根節點
        heapify(arr, n, largest)


#給定一個陣列長度排序
def heapSort(arr):
    n = len(arr) #陣列長度

    #建立一個maxheap.
    for i in range(n, -1, -1): #從第n個開始，遞減，到第0個
        heapify(arr, n, i)

    #一個一個取出元素
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]   # swap
        heapify(arr, i, 0)


arr = [12, 11, 13, 5, 6, 7]
heapSort(arr)
n = len(arr)
print(arr)
