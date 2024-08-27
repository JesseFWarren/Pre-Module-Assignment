# Jesse Warren Pre-Module Assignment 8/25
import unittest
import csv_filter
import pandas as pd

class TestFilter(unittest.TestCase):

    def setUp(self):
        self.input = 'test_input.csv' #Create a test input file with several rows
        sample_data = { #Create sample data for input
            'name': ['Jesse', 'Ethan', 'Reed', 'Marc', 'Richie'],
            'age': [22, 21, 22, 23, 21],
            'occupation': ['Student', 'Student', 'Chemical Engineer', 'Software Engineer', 'Student']
        }
        df = pd.DataFrame(sample_data)
        df.to_csv(self.input, index=False) #Convert data to df
        self.output = 'test_output.csv' #create the test output file 
   
    def test_filer(self):
        """
        Test filtering by occupation "Student", should return only 3 rows
        in which the age column is "Student". The dataframes are compared with
        assert_frame_equal
        """
        csv_filter.filter(self.input, self.output, 'Student', 'occupation') #Run the operation

        #Create expected data for output to compare to actual
        expected = {
            'name': ['Jesse', 'Ethan', 'Richie'],
            'age': [22, 21, 21],
            'occupation': ['Student', 'Student', 'Student']
        }
        expectedDf = pd.DataFrame(expected)
        outputDf = pd.read_csv(self.output) #Read output csv to df for comparison

        pd.testing.assert_frame_equal(expectedDf, outputDf) #compare dataframes


if __name__ == "__main__":
    unittest.main()
