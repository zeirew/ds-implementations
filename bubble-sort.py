## O(n^2) in worst & average case
def perform_bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if(array[j] > array[j+1]):
                array[j], array[j+1] = array[j+1], array[j]
    return array


print(perform_bubble_sort([87, 234, -1, 0, 22]))