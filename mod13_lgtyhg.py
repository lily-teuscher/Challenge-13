import unittest
from datetime import datetime

#Symbol
class Symbol(unittest.TestCase):
    #arrage
    def setUp(self):
        self.input = input("Enter Stock Symbol: ")
    #testing capitalization
    def test_isupper(self): 
        self.assertTrue(self.input.isupper())
    #testing 1-7 alpha characters       
    def test_isalpha_and_7characters(self): 
        self.assertTrue(self.input.isalpha())

#Chart Type
class chartType(unittest.TestCase):
    #arrange
    def setUp(self): 
        self.input = input("Enter Chart Type (1 or 2): ")
    #testing length of input is 1 numeric character
    def test_1numeric(self): 
        if self.input == int and self.input.len() == 1: 
            return self.input
        else: 
            return ("Error")
    #testing input is 1 or 2 
    def test_1_or_2(self):
        if self.input == 1 or self.input == 2: 
            return self.input
        else: 
            return("Error")

#Time Series
class timeSeries(unittest.TestCase): 
    #arrage
    def setUp(self): 
        self.input = input("Enter Time Series (1-4): ")
    #testing for one numeric input
    def test_1numeric(self): #fix
        if self.input == int and self.input.len() == 1: 
            return self.input
        else: 
            return("Error")
    #testing for an input 1-4
    def test_1through4(self): #fix
        if self.input == 1 or self.input == 2 or self.input == 3 or self.input == 4: 
            return self.input
        else: 
            return("Error")

#Start Date
class startDate(unittest.TestCase): 
    #arrange
    def setUp(self): 
        self.input = input("Enter Start Date")
    #testing that the format is correct
    def test_dateType(self): 
        try: 
            datetime.strptime(self.input, '%yyyy-%mm-%dd')
        except ValueError: 
            raise ValueError("Error: Please enter a date in this format: YYYY-MM-DD: ")

#End Date      
class endDate(unittest.TestCase):
    #arrage
    def setUp(self): 
        self.input = input("Enter End Date: ")
    #testing that the format is correct
    def test_dateType(self): 
        try: 
            datetime.strptime(self.input, '%yyy-%mm-%dd')
        except ValueError: 
            raise ValueError("Error: Please enter a date in this format: YYYY-MM-DD: ")
        
#main
if __name__ == "__main__": 
    unittest.main()


 
