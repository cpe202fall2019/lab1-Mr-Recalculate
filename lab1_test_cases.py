import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter_empty(self):
        """tests if loop raises ValueError if empty list is passed in"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_max_list_iter_all_zero(self):
        """tests for max value when all ints in a list are 0"""
        tlist = [0,0,0,0,0,0,0,0,0,0,0,0]
        self.assertEqual(max_list_iter(tlist), 0)

    def test_max_list_iter_sorted_list_ascending(self):
        """tests for max value when ints in list are sorted
        in ascending order"""
        tlist = [-9999,1,2,3,4,5,6,7,8,9,9999]
        self.assertEqual(max_list_iter(tlist), 9999)

    def test_max_list_iter_sorted_list_decending(self):
        """tests for max value when ints in list are sorted
        in decending order"""
        tlist = [9999,9,8,7,6,5,4,3,2,1,-9999]
        self.assertEqual(max_list_iter(tlist), 9999)

    def test_reverse_rec_empty(self):
        """tests if recursive function raises ValueError if empty list is passed in"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(tlist)

    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])

    def test_reverse_rec_zeros(self):
        self.assertEqual(reverse_rec([0,0,0,0,0,0,0]),[0,0,0,0,0,0,0])

    def test_reverse_rec_gross(self):
        self.assertEqual(reverse_rec([-4,5,-7,-9,3,1,2,-100]),[-100,2,1,3,-9,-7,5,-4])

    def test_bin_search_empty(self):
        """tests if recursive function raises ValueError if empty list is passed in"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            bin_search(0, 0, 0, tlist)

    def test_bin_search_no_target(self):
        #does bin_search return None if it fails to find target?
        list_val =[0,1,2,3,5,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, low, high, list_val), None)

    def test_bin_search_beginning_even(self):
        #does bin_search return the index of a target at the beginning of a list
        #with an even amount of entries?
        list_val =[0,1,2,3,5,7,8,9,10,11]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(0, low, high, list_val), 0)

    def test_bin_search_beginning_odd(self):
        #does bin_search return the index of a target at the beginning of a list
        #with an odd amount of entries?
        list_val =[0,1,2,3,5,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(0, low, high, list_val), 0)

    def test_bin_search_end_even(self):
        #does bin_search return the index of a target at the end of a list
        #with an even amount of entries?
        list_val =[0,1,2,3,5,7,8,9,10,11]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(10, low, high, list_val), 8)

    def test_bin_search_end_odd(self):
        #does bin_search return the index of a target at the end of a list
        #with an odd amount of entries?
        list_val =[0,1,2,3,5,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(10, low, high, list_val), 8)

    def test_bin_search_even(self):
        #does bin_search return the index of a target in the middle of a list
        #with an even amount of entries?
        list_val =[0,1,2,3,4,7,8,9,10,11]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, low, high, list_val), 4)

    def test_bin_search_odd(self):
        #does bin_search return the index of a target in the middle of a list
        #with an odd amount of entries?
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, low, high, list_val), 4)

if __name__ == "__main__":
        unittest.main()

    
