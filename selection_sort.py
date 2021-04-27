def findSmallestIndex(list):
    sValue=list[0]
    sIndex=0
    for i in range(1,len(list)):
        if list[i]<sValue:
            sValue=list[i]
            sIndex=i
    return sIndex


def selection_sort(list):
    nlist=[]
    for _ in range(len(list)):
        index=findSmallestIndex(list)
        nlist.append(list.pop(index))
    return nlist

print(selection_sort([5,6,2,3,1]))
