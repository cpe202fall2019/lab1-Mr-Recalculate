"""finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
def max_list_iter(int_list):  # must use iteration not recursion
    if not int_list:
        raise ValueError('list is empty') 
    temp = int_list[0]
    for x in range(len(int_list)):
        if int_list[x] > temp:
            temp = int_list[x]
    return temp


# must use recursion
"""recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
def reverse_rec(int_list, idx=0):   
   if not int_list:
       raise ValueError('list is empty') 
   watch = len(int_list)//2
   if idx >= len(int_list)//2:
       return int_list
   #swaps values in opposite ends of list 
   temp = int_list[len(int_list)-1-idx]
   int_list[len(int_list)-1-idx] = int_list[idx]
   int_list[idx] = temp
   #increments idx
   idx = idx+1
   #recursivly called reverse_rec to swap next pair of values
   #which are incremental one index closer together
   reverse_rec(int_list, idx)
   return int_list

# must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
def bin_search(target, low, high, int_list):  
   if not int_list:
       raise ValueError('list is empty')
   idx = (low+high)//2
   if int_list[idx] == target:
       return idx
   elif int_list[high] == target:
      return high
   elif low+1 == high:
       return None
   #if target is bigger than value at idx
   elif int_list[idx] < target:
       return bin_search(target, idx, high, int_list)
    #if target is smaller than value at idx
   elif int_list[idx] > target:
       return bin_search(target, low, idx, int_list)
       
