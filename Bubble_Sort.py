def bubble_sort(list):
    hasChange = 1
    while (hasChange == 1):
        i = 0
        hasChange = 0
        while(i < len(list) - 1):
            if (list[i] > list[i+1]):
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
                hasChange = 1
            i += 1
    return(list)

##list = [12,34,2,78,1,8,4,12,1002,0,46,1]
##sorted_list = bubble_sort(list)
##print(sorted_list)