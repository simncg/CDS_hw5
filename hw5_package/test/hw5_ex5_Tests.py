import unittest
import pytest
from pandas.util.testing import assert_frame_equal
from hw5_library.hw5_ex5_Caicedo_Eslava_Stassinos import *
import pandas as pd

# TESTS 

class Test_HW5(unittest.TestCase):
    
    # Exercise 1
    def test_car_at_light(self):
        colors = ['red', 'yellow','green']
        output = list(map(car_at_light, colors))
        expected_output = ['stop', 'wait', 'go']
        self.assertEqual (output,expected_output)
        with self.assertRaises(Exception):
             car_at_light('brown')
    
    # Exercise 2
    def test_safe_subtract(self):
        x, y = 10, 5
        output = safe_subtract(x,y)
        expected_output = -5
        self.assertEqual(output,expected_output)
        self.assertIsNone(safe_subtract('x', y))
        with self.assertRaises(Exception):
            safe_subtract(1, 2/0)
        
    #Exercise 3
    
    def test_retrieve_age_eafp(self):
        output=retrieve_age_eafp({'name': 'John', 'last_name': 'Doe', 'birth': 1987})
        expected_output=34
        self.assertEqual(output,expected_output)
        with self.assertRaises(KeyError):
            retrieve_age_eafp({'name': 'Janet', 'last_name': 'Bird', 'gender': 'female'})
    def test_retrieve_age_lbyl(self):
        output=retrieve_age_lbyl({'name': 'John', 'last_name': 'Doe', 'birth': 1987})
        expected_output=34
        self.assertEqual(output,expected_output)
        with self.assertRaises(KeyError):
            retrieve_age_lbyl({'name': 'Janet', 'last_name': 'Bird', 'gender': 'female'})

    # Exercise 4
    
    def test_read_data(self):
        expected_output = pd.read_csv("sample_diabetes_mellitus_data.csv")
        output = read_data("sample_diabetes_mellitus_data.csv")
        assert_frame_equal(output, expected_output)
        with self.assertRaises(FileNotFoundError):
            read_data("DSKDKJ.csv")
            
    # Exercise 5
            
    def test_count_simba(self):
        simba_l = ['Simba', 'Other', 'Simba and Other', 'Simbas', 'Friend Simba']
        output = count_simba(simba_l)
        expected_output = 3
        self.assertEqual(output, expected_output)
    
    # Exercise 7 
    def test_get_day_month_year(self):
        dates = [datetime.datetime(2021, 11, 14), datetime.datetime(2021, 11, 13)]
        output = get_day_month_year(dates)
        # do we want numbers to be objects or int??
        expected_output = pd.DataFrame({'day': ['14', '13'], 'month': ['11', '11'], 'year': ['2021', '2021']})
        # not sure if this works with unittest
        assert_frame_equal(output, expected_output)
        
    # Exercise 8
    def test_compute_distance(self):
        loc = [((41.23,23.5), (41.5, 23.4)), ((52.38, 20.1), (52.3, 17.8))]
        output = compute_distance(loc)
        expected_output = [distance.distance(loc[0][0], loc[0][1]).km, distance.distance(loc[1][0], loc[1][1]).km]   
        self.assertEqual(output, expected_output)
        
    
    
    def test_sum_general_int_list(self):
        list_t = [[2], 3, [[1,2],5]] 
        output = sum_general_int_list(list_t)
        expected_output = 13
        self.assertEqual(output, expected_output)
                 
            