#a = [ int(i)for i in input().split()]
a = list(map(int,input().split()))
b = list(map(int,input().split()))

def merge_two_list(a:list,b:list)->list:
    
    while 