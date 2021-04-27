def quick_sort(list):
    if len(list)<2:
        return list
    pivot=list[0]
    smallList=[i for i in list[1:] if i<=pivot]
    bigList=[i for i in list[1:] if i>pivot]
    return quick_sort(smallList)+[pivot]+quick_sort(bigList)




print(quick_sort([5,6,2,3,1]))