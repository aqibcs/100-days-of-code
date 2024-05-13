# Fibonacci Series
def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Driver Code
n_terms = 10
print("Fibonacci Series:")
for i in range(1, n_terms + 1):
    print(fibonacci(i), end=" ")


# Binary Search
def binary_search(arr, target, low, high):
    if low > high:
        return  -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return  mid
    elif arr[mid] > target:
        return  binary_search(arr, target, low, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, high)


# Driver Code
arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 23
result = binary_search(arr, target, 0, len(arr) - 1)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")