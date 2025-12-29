a = list(map(int, input().split()))
b = list(map(int, input().split()))


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


