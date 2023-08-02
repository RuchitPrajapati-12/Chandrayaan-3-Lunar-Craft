import unittest
from Chandrayan_Spacecraft import Spacecraft

class TestSpacecraft(unittest.TestCase):

    def test_initial_position_and_direction(self):
        spacecraft = Spacecraft(0, 0, 0, 'N')
        self.assertEqual(spacecraft.x, 0)
        self.assertEqual(spacecraft.y, 0)
        self.assertEqual(spacecraft.z, 0)
        self.assertEqual(spacecraft.direction, 'N')

if __name__ == '__main__':
    unittest.main()