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
def reverse_rec(int_list):   
   if not int_list:
       raise ValueError('list is empty') 
   if len(int_list) == 1:
       return [int_list.pop()]
   temp = [int_list.pop()]
   new_list = int_list
   return temp + reverse_rec(new_list)

# must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
def bin_search(target, low, high, int_list):  
   if not int_list:
       raise ValueError('list is empty')
   idx = (low+high)//2
   #base cases
   if int_list[idx] == target:
       return idx
   #handles low edgecase
   elif int_list[low] == target:
      return low
   #handles high edgecase
   elif int_list[high] == target:
      return high
   #if low and high are the same or one apart, return None
   elif low+1 == high or low == high:
       return None
   #recursive calls
   #if target is bigger than value at idx
   elif int_list[idx] < target:
       return bin_search(target, idx+1, high, int_list)
    #if target is smaller than value at idx
   elif int_list[idx] > target:
       return bin_search(target, low, idx-1, int_list)
       
