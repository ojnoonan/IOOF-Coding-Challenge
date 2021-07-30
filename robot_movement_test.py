# IOOF Coding Challenge 2 Test
# Created By: Oliver Noonan
# Date: 28 Jul 2021

import unittest
from robot_movement import place, move, turn, report


class MyTestCase(unittest.TestCase):

    def test_command_before_place(self):
        self.assertEqual(move(), None)
        self.assertEqual(turn('LEFT'), None)
        self.assertEqual(turn('RIGHT'), None)

    def test_basic_placement(self):
        place('0,0,NORTH')
        self.assertEqual(report(), '[0, 0] NORTH')

    def test_basic_movement(self):
        place('0,0,NORTH')
        move()
        self.assertEqual(report(), '[1, 0] NORTH')

    def test_basic_turn_right(self):
        place('0,0,NORTH')
        turn('RIGHT')
        self.assertEqual(report(), '[0, 0] EAST')

    def test_basic_turn_left(self):
        place('0,0,NORTH')
        turn('LEFT')
        self.assertEqual(report(), '[0, 0] WEST')

    def test_advanced_movement(self):
        place('3,3,SOUTH')
        move()
        move()
        turn('RIGHT')
        self.assertEqual(report(), '[1, 3] WEST')


if __name__ == '__main__':
    unittest.main()
