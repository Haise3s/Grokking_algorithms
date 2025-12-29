a = list(map(int, input().split()))


def sort_sel(a):
    n = len(a)
    for i in range(n - 1):
        m_i = i
        for j in range(i + 1, n):
            if a[j] < a[m_i]:
                m_i = j
        a[i], a[m_i] = a[m_i], a[i]
    return a


print(sort_sel(a))
