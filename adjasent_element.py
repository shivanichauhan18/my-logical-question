count=[]
def adjacentElementsProduct(inputArray):
    i=0
    sum=0
    j=i+1
    while j<len(inputArray):
        sum=inputArray[i]*inputArray[j]
        count.append(sum)
        i=i+1
        j=j+1
    b=0
    largest=count[b]
    while b<len(count):
        if count[b]>largest:
            largest=count[b]
        b=b+1
    return largest
print adjacentElementsProduct([-23, 4, -3, 8, -12])
    