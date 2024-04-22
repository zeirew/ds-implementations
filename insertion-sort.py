## O(n^2) in worst case
## O(n) in best case (already sorted)
def perform_insertion_sort(array):
    for curr in range(1, len(array)):
        prev = curr - 1
        curr_value = array[curr]

        while(prev > -1 and array[prev] > curr_value):
            array[prev + 1] = array[prev]
            prev -= 1
        
        array[prev + 1] = curr_value

    return array


print(perform_insertion_sort([87, 234, -1, 0, 22]))