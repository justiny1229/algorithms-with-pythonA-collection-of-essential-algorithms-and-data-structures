"""
Efficient Sorting Algorithms
"""

# MERGE SORT
# Time Complexity: O(n log n) - Stable and consistent
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Divide
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Conquer (Merge)
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# --- TEST ---
if __name__ == "__main__":
    unsorted_list = [38, 27, 43, 3, 9, 82, 10]
    print(f"Original: {unsorted_list}")
    sorted_list = merge_sort(unsorted_list)
    print(f"Sorted:   {sorted_list}")
