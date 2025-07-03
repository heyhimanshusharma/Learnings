import unittest
from city_functions import get_formatted_name

class NameTestCase(unittest.TestCase):
    def test_city_country_name(self):
        formatted_name = get_formatted_name('pune', 'india')
        self.assertEqual(formatted_name, 'Pune India')
    
    def test_city_country_population(self):
        formatted_name = get_formatted_name('pune', 'india', 7500000)
        self.assertEqual(formatted_name, 'Pune India 7500000')

if __name__ == '__main__':
    unittest.main()