def binary_search(arr, val, low, high):
    if high >= low:
        mid = (low + high) // 2

        if arr[mid] == val:
            return True
        if arr[mid] < val:
            return binary_search(arr, val, mid + 1, high)
        if arr[mid] > val:
            return binary_search(arr, val, low, mid - 1)
    else:
        return False


def has_intersection(set1, set2):
    if len(set1) > len(set2):
        sorted_set = sorted(set2)

        return any(
            binary_search(sorted_set, val, 0, len(sorted_set) - 1) for val in set1
        )
    else:
        sorted_set = sorted(set1)

        return any(
            binary_search(sorted_set, val, 0, len(sorted_set) - 1) for val in set2
        )


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]

    print(binary_search(arr, 6, 0, len(arr) - 1))

    assert binary_search(arr, 1, 0, len(arr) - 1)
    assert binary_search(arr, 2, 0, len(arr) - 1)
    assert binary_search(arr, 3, 0, len(arr) - 1)
    assert binary_search(arr, 4, 0, len(arr) - 1)
    assert binary_search(arr, 5, 0, len(arr) - 1)
    assert not binary_search(arr, 6, 0, len(arr) - 1)
    assert not binary_search(arr, -1, 0, len(arr) - 1)

    assert has_intersection({1, 2, 3}, {1, 2, 3})
    assert has_intersection({1, 2, 3}, {1})
    assert has_intersection({1}, {1, 2, 3})
    assert has_intersection(
        {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, {4, 7, 8, 10, 2, 1, 3, 5, 7, 6}
    )
    assert not has_intersection({1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, {11})
    assert not has_intersection({11}, {1, 2, 3, 4, 5, 6, 7, 8, 9, 10})
