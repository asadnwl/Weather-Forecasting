import unittest
from unittest.mock import patch
from weather import get_data_from_file
from weather import write_into_file

class test_weather_forecasting(unittest.TestCase):
#arrage
    def setUp(self):
        self.file_path = "data.json"
        self.msg = "msg"
#act
    def test_weather(self):
        result = get_data_from_file(self.file_path)
        result1 = write_into_file(self.msg)
#asert
        assert len(result) != 0 
        assert len(result1) != 0





if __name__ == "__main__":
    unittest.main()