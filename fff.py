def median(lst):
    sortedLst = sorted(lst)
    lstLen = len(lst)
    print(lstLen)
    index = (lstLen - 1) // 2
    print(index)
   
    if (lstLen % 2):
        return sortedLst[index]
    else:
        return (sortedLst[index] + sortedLst[index + 1])/2.0
    


x = median([3])
print(x)