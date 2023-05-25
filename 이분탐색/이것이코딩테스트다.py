#7.1

#7-2
def binary_search (arr, tar, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if arr[mid] == tar:
        return mid
    elif arr[mid] > tar:
        return binary_search(arr, tar, start, end-1)
    else:
        return binary_search(arr, tar, mid+1, end)


