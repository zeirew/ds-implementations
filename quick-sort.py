import random

## O(n^2) in worst case (picks largest or smallest element as pivot every time)
## O(n*(log(n))) in average/best case (chooses middle element as pivot)
## Space Complexity: O(n) in worst case, O(log(n)) in best case since when subarrays are 1/2 of array, which results in log(n) recursive calls
def perform_quick_sort(array, start, end):
    if start < end:
        pivot_index = partition(array, start, end)
        perform_quick_sort(array, start, pivot_index - 1)
        perform_quick_sort(array, pivot_index + 1, end)

def partition(array, start, end):
    pivot = array[end] #rightmost element will be pivot

    i = start - 1 #index of last item < pivot (that we've looked at)

    for j in range(start, end):
        if(array[j] <= pivot):
            i += 1 #increase bound of less-than-pivot items
            array[i], array[j] = array[j], array[i] #swap 
    

    #swap pivot with first 'greater' element
    array[i+1], array[end] = array[end], array[i+1]

    #return pivot index
    return i+1

array = [87, 234, -1, 0, 22]
perform_quick_sort(array, 0, len(array) - 1)
print(array)