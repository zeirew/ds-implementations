## Time Complexity: O(n*log(n)) in all cases
## Space Complexity: O(n)
def perform_merge_sort(array):
    if(len(array) <= 1):
        return array
    
    mid_index = len(array)//2 
    left_list = array[:mid_index] #up till & not including mid_index
    right_list = array[mid_index:] #mid_index to last element of list

    left = perform_merge_sort(left_list)
    right = perform_merge_sort(right_list)

    return merge(left, right)

def merge(left, right):
    l = 0
    r = 0
    merged = []

    while l < len(left) and r < len(right):
        l_val = left[l]
        r_val = right[r]
        
        if(l_val <= r_val):
            merged.append(l_val)
            l+=1
        else:
            merged.append(r_val)
            r+=1

    while l < len(left):
        merged.append(left[l])
        l+=1

    while r < len(right):
        merged.append(right[r])
        r+=1
    
    return merged
            
print(perform_merge_sort([87, 234, -1, 0, 22]))