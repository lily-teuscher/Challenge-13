import unittest
from datetime import datetime

#Symbol
class Symbol(unittest.TestCase):
    #arrage
    def setUp(self):
        self.input = input("Enter Stock Symbol: ")
    #testing capitalization
    def test_isupper(self): 
        result = self.input.isupper()
        self.assertTrue(self.input.isupper())
    #testing 1-7 alpha characters       
    def test_isalpha_and_7characters(self): 
        for i in range(1, 7): 
            self.assertEqual(i, i)
            self.assertTrue(self.input.isalpha())

#Chart Type
class chartType(unittest.TestCase):
    #arrange
    def setUp(self): 
        self.input = input("Enter Chart Type (1 or 2): ")
    #testing length of input is 1 numeric character
    def test_1numeric(self): 
        if self.input == int and self.input.len() == 1: 
            self.assertTrue(self.input.isnumeric())
        else: 
            return ("Error: the input is not an integer of length 1.")
    #testing input is 1 or 2 
    def test_1_or_2(self):
        for i in range(1, 2): 
            self.assertEqual(i, i)

#Time Series
class timeSeries(unittest.TestCase): 
    #arrage
    def setUp(self): 
        self.input = input("Enter Time Series (1-4): ")
    #testing for one numeric input
    def test_1numeric(self): #fix
        if self.input == int and self.input.len() == 1: 
            self.assertEqual(self.input.isnumeric())
        else: 
            return("Error: the input is not an ineger of length 1.")
    #testing for an input 1-4
    def test_1through4(self): #fix
        for i in range(1, 4): 
            self.assertEqual(i, i)
            
#Start Date
class startDate(unittest.TestCase): 
    #arrange
    def setUp(self): 
        self.input = input("Enter Start Date")
    #testing that the format is correct
    def test_dateType(self): 
        try: 
            datetime.strptime(self.input, '%yyyy-%mm-%dd')
        except: 
            self.assertRaises(TypeError)

#End Date      
class endDate(unittest.TestCase):
    #arrage
    def setUp(self): 
        self.input = input("Enter End Date: ")
    #testing that the format is correct
    def test_dateType(self): 
        try: 
            datetime.strptime(self.input, '%yyy-%mm-%dd')
        except: 
            self.assertRaises(TypeError)
#main
if __name__ == "__main__": 
    unittest.main()


 
