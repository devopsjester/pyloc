import unittest
from locate_me import get_location

class TestLocateMe(unittest.TestCase):
    
    def test_get_location(self):
        self.assertEqual(get_location('90210'), ('Beverly Hills', 'California'))
        self.assertEqual(get_location('10001'), ('New York City', 'New York'))
        self.assertEqual(get_location('60601'), ('Chicago', 'Illinois'))
        self.assertEqual(get_location('94102'), ('San Francisco', 'California'))
        self.assertEqual(get_location('75201'), ('Dallas', 'Texas'))
        self.assertEqual(get_location('98101'), ('Seattle', 'Washington'))
        self.assertEqual(get_location('30303'), ('Atlanta', 'Georgia'))
        self.assertEqual(get_location('02108'), ('Boston', 'Massachusetts'))
        self.assertEqual(get_location('20001'), ('Washington', 'District of Columbia'))
        self.assertEqual(get_location('33109'), ('Miami Beach', 'Florida'))
        
if __name__ == '__main__':
    unittest.main()