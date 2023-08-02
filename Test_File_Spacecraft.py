import unittest
from Chandrayan_Spacecraft import Spacecraft

class TestSpacecraft(unittest.TestCase):

    def test_initial_position_and_direction(self):
        spacecraft = Spacecraft(0, 0, 0, 'N')
        self.assertEqual(spacecraft.x, 0)
        self.assertEqual(spacecraft.y, 0)
        self.assertEqual(spacecraft.z, 0)
        self.assertEqual(spacecraft.direction, 'N')

    def test_move_forward(self):
        spacecraft = Spacecraft(0, 0, 0, 'N')
        spacecraft.move_forward()
        self.assertEqual(spacecraft.y, 1)

    def test_move_backward(self):
        spacecraft = Spacecraft(0, 0, 0, 'N')
        spacecraft.move_backward()
        self.assertEqual(spacecraft.y, -1)

    def test_turn_left(self):
        spacecraft = Spacecraft(0, 0, 0, 'N')
        spacecraft.turn_left()
        self.assertEqual(spacecraft.direction, 'W')

    def test_turn_right(self):
        spacecraft = Spacecraft(0, 0, 0, 'N')
        spacecraft.turn_right()
        self.assertEqual(spacecraft.direction, 'E')

    def test_turn_up(self):
        spacecraft = Spacecraft(0, 0, 0, 'N')
        spacecraft.turn_up()
        self.assertEqual(spacecraft.direction, 'Up')

    def test_turn_down(self):
        spacecraft = Spacecraft(0, 0, 0, 'N')
        spacecraft.turn_down()
        self.assertEqual(spacecraft.direction, 'Down')


if __name__ == '__main__':
    unittest.main()