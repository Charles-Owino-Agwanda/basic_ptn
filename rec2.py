def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        left = merge_sort(left)
        right = merge_sort(right)

        merged = []
        while len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                merged.append(left.pop(0))
            else:
                merged.append(right.pop(0))

        merged = merged + left + right

        return merged
    else:
        return arr


arr = [5, 4, 9, 11, 17, 1, 3, 5]
print(merge_sort(arr))
