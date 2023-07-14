import unittest
from locate_me import get_location

class TestLocateMe(unittest.TestCase):
    
    def test_beverly_hills(self):
        self.assertEqual(get_location('90210'), ('Beverly Hills', 'California'))
        
    def test_new_york_city(self):
        self.assertEqual(get_location('10001'), ('New York City', 'New York'))
        
    def test_chicago(self):
        self.assertEqual(get_location('60601'), ('Chicago', 'Illinois'))
        
    def test_san_francisco(self):
        self.assertEqual(get_location('94102'), ('San Francisco', 'California'))
        
    def test_dallas(self):
        self.assertEqual(get_location('75201'), ('Dallas', 'Texas'))
        
    def test_seattle(self):
        self.assertEqual(get_location('98101'), ('Seattle', 'Washington'))
        
    def test_atlanta(self):
        self.assertEqual(get_location('30303'), ('Atlanta', 'Georgia'))
        
    def test_boston(self):
        self.assertEqual(get_location('02108'), ('Boston', 'Massachusetts'))
        
    def test_washington_dc(self):
        self.assertEqual(get_location('20001'), ('Washington', 'District of Columbia'))
        
    def test_miami_beach(self):
        self.assertEqual(get_location('33109'), ('Miami Beach', 'Florida'))

if __name__ == '__main__':
    unittest.main()