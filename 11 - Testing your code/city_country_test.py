import unittest
from city_functions import city_country

class cityTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'"""

    def test_city_country(self):
        """Do city names like 'Santiago, Chile' work?"""
        city = city_country('santiago', 'chile')
        self.assertEqual(city, 'Santiago, Chile')

    def test_city_country_population(self):
        """Do city names like 'Santiago, Chile - population 5000000' work?"""
        city = city_country('santiago', 'chile', '5000000')
        self.assertEqual(city, 'Santiago, Chile - population 5000000')


if __name__ == '__main__':
    unittest.main()