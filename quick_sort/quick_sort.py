import random
import time

a = [random.randint(-100, 100) for _ in range(10)]


def quick_sort(a):
    n = len(a)
    if n <= 1:
        return a
    pivot = random.choice(a)
    left, center, right = [], [], []
    for i in a:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
        else:
            center.append(i)
    return quick_sort(left) + center + quick_sort(right)

time_start = time.time()
print(quick_sort(a))
time_end = time.time()
print(f'{(time_end - time_start):.8f}')