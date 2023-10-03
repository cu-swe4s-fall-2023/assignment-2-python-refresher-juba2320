import sys 
sys.path.insert(0,'../../src')
import my_utils
import unittest
from random import randint
import statistics

class TestCalc(unittest.TestCase):
    # mean test cases
    def test_find_mean_positive_case(self):
        array = [1,2,3,4,5]
        self.assertEqual(my_utils.find_mean(array),3)
    
    def test_find_mean_negative_case(self):
        array = [-1,-2,3,4,-10]
        self.assertEqual(my_utils.find_mean(array),-1.2)

    def test_find_mean_random(self):
        for i in range(100):
            array = [randint(1,100),randint(-5,100),randint(-20,100),randint(1,100)]
            self.assertEqual(my_utils.find_mean(array),statistics.mean(array))
    
    # median test cases 
    def test_find_median_positive_case_odd_num(self):
        array = [9,7,10,12,1]
        self.assertEqual(my_utils.find_median(array),9)
    
    def test_find_median_positive_case_even_num(self):
        array = [5,4,2,10]
        self.assertEqual(my_utils.find_median(array),4.5)
        
    def test_find_median_negative_case(self):
        array = [-1,4,-6,9]
        self.assertEqual(my_utils.find_median(array),1.5)
    
    def test_find_median_random(self):
        for i in range(100):
            array = [randint(-100,100),randint(1,100),randint(-10,100),randint(1,100),randint(20,100),randint(-8,100)]
            self.assertEqual(my_utils.find_median(array), statistics.median(array))
    
    # standard deviation test cases 
    def test_find_sd_positive_case_sizable_array(self):
        array = [10,10,14,16]
        self.assertEqual(my_utils.find_sd(array), 3)
        
    def test_find_sd_positive_case_small_array(self):
        array = [2]
        self.assertEqual(my_utils.find_sd(array), 0)
    
    def test_find_sd_negative_case(self):
        array = [-5,-4,-1,-7]
        self.assertEqual(my_utils.find_sd(array), 2.5)
    
    def test_find_sd_random_case(self):
        for i in range(100):
            array = [randint(-8,100),randint(1,100),randint(-100,100),randint(-40,100),randint(5,100)]
            self.assertEqual(round(my_utils.find_sd(array),12), round(statistics.stdev(array),12))

if __name__ == 'main':
    unittest.main()