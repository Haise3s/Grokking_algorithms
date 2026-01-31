a = list(map(str, input().split()))
#b = list(map(int, input().split()))


def merge_two_list(a: list, b: list) -> list:
    i = j = 0
    new = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            new.append(a[i])
            i += 1
        else:
            new.append(b[j])
            j += 1
    if i < len(a):
        new += a[i:]
    if j < len(b):
        new += b[j:]
    return new

def merge_sort(a):
    if len(a) == 1:
        return a
    mid = len(a)//2
    left = merge_sort(a[0:mid])
    right = merge_sort(a[mid:])
    return merge_two_list(left,right)

print(merge_sort(a))

 