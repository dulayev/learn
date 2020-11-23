# 0.53 sec -> 0.45 sec -> 0.035 sec

import time
start = time.time()

import random
arr = [5, 9, 4, 14, 15, 11, 8, 11, 14, 17, 14, 4, 17, 0, 3, 4, 1, 2, 10, 10]
arr = [5, 3, 4, 4, 2]
#arr = [random.randrange(100000) for _ in range(100000)]

lists = [] # of tuple(ref to tuple, last index)

def min_end(lists):
    return lists[-1]

def max_end(lists):
    return lists[0]

def longest(lists):
    return lists[-1]

def longest_can_continue(lists, a):
    left = 0
    right = len(lists)

    while right - left > 1:
        middle = (left + right) // 2
        if arr[lists[middle][-1]] >= a:
            left = middle
        else:
            right = middle
        #print("lr:", left, right)
    return left

def longest_can_continue2(lists, a):
    return longest([l for l in lists if arr[l[-1]] >= a])

for i, a in enumerate(arr):
    if not lists:
        lists.append((None, i))
    elif a > arr[max_end(lists)[-1]]:
        lists[0] = (None, i)
    else:
        min_end_list = longest(lists)
        if a <= arr[min_end_list[-1]]:
            lists.append((min_end_list, i))
        else:
            min_end_list_index = longest_can_continue(lists, a)
            min_end_list = lists[min_end_list_index]
            #print("insert: ", min_end_list_index)
            lists[min_end_list_index + 1] = (min_end_list, i)
    #print(i, a, lists)

last = lists[-1]
best = [last[-1]]

while last[0] != None:
    last = last[0]
    best.append(last[-1])

best = best[::-1]
print((time.time() - start), " passed")

print(len(best))
print(*best)
print(*[arr[i] for i in best])
