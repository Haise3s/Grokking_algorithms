#a = [ int(i)for i in input().split()]
a = list(map(int,input().split()))
b = list(map(int,input().split()))

def merge_two_list(a:list,b:list)->list:
    new_list = []
    i = j = 0
    while i<len(a) and j < len(b):
        if a[i] < b[j]:
            new_list.append(a[i])
            i +=1
        else:
            new_list.append(b[j])
            j +=1
    if i < len(a):
        new_list += a[i:]
    if j < len(b):
        new_list += b[j:]
    return new_list


print(merge_two_list(a,b))