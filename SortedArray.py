arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

union = sorted(set(arr1) | set(arr2))
print("Union:", union)
