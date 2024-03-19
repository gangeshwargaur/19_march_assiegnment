# Framework: JUnit, ThoughtWorks Rover
# Technology Stack: Java

from assiegnment.rover.commands import RotateLeftCommand
from assiegnment.rover import MarsRover
from assiegnment.rover.universe import Coordinates, Direction, Plateau
import unittest

class RotateLeftCommandTest(unittest.TestCase):

    def test_that_rotate_left_command_rotates_the_navigable_object_left(self):
        # Given
        command = RotateLeftCommand()
        plateau = Plateau(5, 5)
        starting_position = Coordinates(1, 2)
        rover = MarsRover(plateau, Direction.N, starting_position)

        # When
        command.execute(rover)

        # Then
        self.assertEqual("1 2 W", rover.current_location())