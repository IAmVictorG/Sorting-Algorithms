def quick_sort(list):
    if (len(list) <= 1):
        return list
    pivot = list[0]
    del (list[0])
    ##print(pivot)
    list1 = []
    list2 = []
    for e in list:
        if (e < pivot):
            list1.append(e)
        else:
            list2.append(e)
    return quick_sort(list1) + [pivot] + quick_sort(list2)

list = [12,34,2,78,1,8,4,12,1002,0,46,1]
sorted_list = quick_sort(list)
print(sorted_list)