
from assiegnment.rover.commands import RotateRightCommand
from assiegnment.rover import MarsRover
from assiegnment.rover.universe import Coordinates, Direction, Plateau
import unittest

class RotateRightCommandTest(unittest.TestCase):

    def test_that_rotate_right_command_rotates_the_navigable_object_right(self):
        # Given
        command = RotateRightCommand()
        plateau = Plateau(5, 5)
        starting_position = Coordinates(1, 2)
        rover = MarsRover(plateau, Direction.N, starting_position)

        # When
        command.execute(rover)

        # Then
        self.assertEqual("1 2 E", rover.current_location())