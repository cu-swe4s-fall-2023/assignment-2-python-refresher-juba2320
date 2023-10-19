import sys
sys.path.insert(0, '../../src')
import my_utils
import unittest
from random import uniform
import statistics
import os


class TestCalc(unittest.TestCase):
    # mean test cases
    def test_find_mean_positive_case(self):
        array = [1, 2, 3, 4, 5]
        self.assertEqual(my_utils.find_mean(array), 3)

    def test_find_mean_negative_case(self):
        array = [-1, -2, 3, 4, -10]
        self.assertEqual(my_utils.find_mean(array), -1.2)

    def test_find_mean_random(self):
        for i in range(100):
            array = [uniform(1.0, 100.0), uniform(-5.0, 100.0), uniform(-20.0, 100.0), uniform(1.0, 100.0)]
            self.assertEqual(round(my_utils.find_mean(array), 8), round(statistics.mean(array), 8))

    # median test cases
    def test_find_median_positive_case_odd_num(self):
        array = [9, 7, 10, 12, 1]
        self.assertEqual(my_utils.find_median(array), 9)

    def test_find_median_positive_case_even_num(self):
        array = [5, 4, 2, 10]
        self.assertEqual(my_utils.find_median(array), 4.5)

    def test_find_median_negative_case(self):
        array = [-1, 4, -6, 9]
        self.assertEqual(my_utils.find_median(array), 1.5)

    def test_find_median_random(self):
        for i in range(100):
            array = [uniform(-100.0, 100.0), uniform(1.0, 100.0), uniform(-10.0, 100.0), uniform(1.0, 100.0), uniform(20.0, 100.0), uniform(-8.0, 100.0)]
            self.assertEqual(my_utils.find_median(array), statistics.median(array))

    # standard deviation test cases
    def test_find_sd_positive_case_sizable_array(self):
        array = [10, 10, 14, 16]
        self.assertEqual(my_utils.find_sd(array), 3)

    def test_find_sd_positive_case_small_array(self):
        array = [2]
        self.assertEqual(my_utils.find_sd(array), 0)

    def test_find_sd_negative_case(self):
        array = [-5, -4, -1, -7]
        self.assertEqual(my_utils.find_sd(array), 2.5)

    def test_find_sd_random_case(self):
        for i in range(100):
            array = [uniform(-8.0, 100.0), uniform(1.0, 100.0), uniform(-100.0, 100.0), uniform(-40.0, 100.0), uniform(5.0, 100.0)]
            self.assertEqual(round(my_utils.find_sd(array), 8), round(statistics.stdev(array), 8))

    # graph histogram function test cases
    def test_graph_basic_hist(self):
        data = [100, 9, 79, 59, 2, 58, 42, 77, 47, 81]
        expected_file = "../../doc/test_title.png"
        my_utils.graph_hist(data, "value", "title", expected_file)
        self.assertTrue(os.path.exists(expected_file))


if __name__ == 'main':
    unittest.main()
