"""finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
def max_list_iter(int_list):  # must use iteration not recursion
    if int_list == []:
        raise ValueError('list is empty')
        return None 
    else:
        temp = -1
        for x in int_list:
            if x > temp:
                temp = x
            return temp



def reverse_rec(int_list):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   pass

def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   pass
