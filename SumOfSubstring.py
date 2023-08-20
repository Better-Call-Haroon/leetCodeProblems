def max_subarray_sum(arr):
    if not arr:
        return 0
    
    max_current = max_global = arr[0]
    for x in arr[1:]:
        max_current = max(x, max_current + x)
        max_global = max(max_global, max_current)
    return max_global
