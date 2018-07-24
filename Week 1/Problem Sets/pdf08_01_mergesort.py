def mergeSort(test_list):

    if len(test_list) == 1:
        return test_list

    elif len(test_list) > 1:
        mid = len(test_list) // 2
        left = test_list[:mid]
        right = test_list[mid:]
        mergeSort(left)
        mergeSort(right)

    i=0
    j=0
    k=0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            test_list[k]=left[i]
            i=i+1
        else:
            test_list[k]=right[j]
            j=j+1
        k=k+1

    while i < len(left):
        test_list[k]=left[i]
        i=i+1
        k=k+1

    while j < len(right):
        test_list[k]=right[j]
        j=j+1
        k=k+1

## Testing the mergesort function... ##
test_list = [4,5,6,1,2,3,100,102,3000,4000,1234]
mergeSort(test_list)
assert test_list == [1, 2, 3, 4, 5, 6, 100, 102, 1234, 3000, 4000]
