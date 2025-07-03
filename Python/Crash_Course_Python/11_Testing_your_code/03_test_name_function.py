import unittest 
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for name_function.py"""

    def test_first_last_name(self):
        """Do names like 'janyl geollegue' work?"""
        formatted_name = get_formatted_name('janyl', 'geollegue')
        self.assertEqual(formatted_name, 'Janyl Geollegue')

    def test_first_last_middle_name(self):
        """Do names like 'janyl rebonanza geollegue' work?"""
        formatted_name = get_formatted_name(
            'janyl', 'geollegue', 'rebonanza')
        self.assertEqual(formatted_name, 'Janyl Rebonanza Geollegue')
    
if __name__ == '__main__':
    unittest.main()