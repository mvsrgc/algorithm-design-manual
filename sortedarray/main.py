def binary_search(arr, low, high, key):
    mid = (low + high) // 2

    if key == arr[mid]:
        return mid

    if key > arr[mid]:
        return binary_search(arr, mid + 1, high, key)

    if key < arr[mid]:
        return binary_search(arr, low, mid - 1, key)


def binary_search_for_insert(arr, low, high, target):
    while low < high:
        mid = (low + high) // 2
        if arr[mid] > target:
            high = mid
        else:
            low = mid + 1
    return low


def insert_sorted(arr, key):
    result = []

    for index, el in enumerate(arr):
        result.append(el)

    pos = binary_search_for_insert(result, 0, len(arr), key)

    result[pos:pos] = [key]

    return result


def delete_sorted(arr, n, key):
    pos = binary_search(arr, 0, n - 1, key)

    if pos == -1:
        print("Element not found.")
        return

    for i in range(pos, n - 1):
        arr[i] = arr[i + 1]

    return n - 1


if __name__ == "__main__":
    arr = [5, 6, 7, 8, 9, 24, 46, 89, 150]

    print(f"Current array: {arr}")

    print(f"Index of element {46}: {binary_search(arr, 0, len(arr), 46)}")
    print(f"Element {10} should be inserted at index: {binary_search_for_insert(arr, 0, len(arr), 10)}")

    print(f"Inserting element {151} at index: {binary_search_for_insert(arr, 0, len(arr), 151)}")
    arr = insert_sorted(arr, 151)

    print(f"Current array: {arr}")
