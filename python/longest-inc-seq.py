arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]

lists = []

def min_end(lists):
    return min(lists, key = lambda l : l[-1])

def max_end(lists):
    return max(lists, key = lambda l : l[-1])

def max_end_limited(lists, limit):
    return max(lists, key = lambda l : 0 if l[-1] >= limit else l[-1])

def discard_len(lists, length):
    return [l for l in lists if len(l) != length]

for a in arr:
    if not lists or a < min_end(lists)[-1]:
        lists.append([a])
    else:
        max_end_list = max_end(lists)
        if a > max_end_list[-1]:
            lists.append(max_end_list.copy() + [a])
        else:
            max_end_list = max_end_limited(lists, a)
            lists = discard_len(lists, len(max_end_list) + 1)
            lists.append(max_end_list.copy() + [a])
            
#    print(lists)
best = max(lists, key = lambda l : len(l))
print(len(best))
print(*best)
