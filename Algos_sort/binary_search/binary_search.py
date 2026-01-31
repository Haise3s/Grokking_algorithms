a = list(map(int,input().split()))

def binary_search(a:list,find:int)->int:
    a.sort()
    n = len(a)
    left = 0
    right = n-1
    while left <= right:
        mid = (left+right)//2
        if a[mid] == find:
            return mid
        elif a[mid] > find:
            right = mid - 1
        else:
            left = mid + 1
    return f'not found {find} in the list {a}'

print(binary_search(a,24))