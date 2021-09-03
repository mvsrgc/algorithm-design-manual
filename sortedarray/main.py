def binary_search(arr, low, high, key):
    mid = (low + high) // 2

    if key == arr[mid]:
        return mid

    if key > arr[mid]:
        return binary_search(arr, mid + 1, high, key)

    if key < arr[mid]:
        return binary_search(arr, low, mid - 1, key)


if __name__ == "__main__":
    arr = [5, 6, 7, 8, 9, 24, 46, 89, 150]

    key = 46
    print(binary_search(arr, 0, len(arr) - 1, key))
