import random

def range_list(start, end):
    return list(range(start, end + 1))

def insert(lst, pos, elem):
    lst.insert(pos, elem)
    return lst

def random_sub(lst, k, n):
    return [random.sample(lst, k) for _ in range(n)]

def sortlen(lists):
    return sorted(lists, key=len)

nums = range_list(1, 20)
insert(nums, 0, 0)
sublists = random_sub(nums, 3, 5)
sorted_sub = sortlen(sublists)

print("Range list:", nums)
print("Random sublists:", sublists)
print("Sorted by length:", sorted_sub)