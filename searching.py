"""
Essential Search Algorithms
Language: Python 3
Author: [Your Name]
"""

# 1. BINARY SEARCH
# Time Complexity: O(log n) - Very efficient for sorted arrays
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Target found, return index
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1  # Target not found

# 2. DEPTH FIRST SEARCH (DFS) - Recursive
# Time Complexity: O(V + E) - Standard for graph traversal
def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()
    
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs_recursive(graph, neighbour, visited)

# --- DRIVER CODE TO TEST ---
if __name__ == "__main__":
    # Test Binary Search
    my_list = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    target = 23
    result = binary_search(my_list, target)
    print(f"Binary Search: Found {target} at index {result}")

    # Test DFS
    # Graph represented as an adjacency list
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    print("\nDFS Traversal:")
    dfs_recursive(graph, 'A')

