a = list(map(int, input().split()))


def booble_sort(a: list) -> list:
    n = len(a)
    count = 1
    for i in range(n - 1):
        if count != 0:
            count = 0
            for j in range(n - 1 - i):
                if a[j] > a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
                    count +=1
        else:
            break
    return a


print(booble_sort(a))
