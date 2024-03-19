from assiegnment.rover.MarsRover import MarsRover
from assiegnment.rover.commands.MoveCommand import MoveCommand
from assiegnment.rover.universe.Coordinates import Coordinates
from assiegnment.rover.universe.Direction import Direction
from assiegnment.rover.universe.Plateau import Plateau
import unittest

class MoveCommandTest(unittest.TestCase):
    def testThatMoveCommandMovesTheNavigableObject(self):
        command = MoveCommand()
        plateau = Plateau(5, 5)
        startingPosition = Coordinates(1, 2)
        rover = MarsRover(plateau, Direction.N, startingPosition)
        
        command.execute(rover)
        
        self.assertEqual("1 3 N", rover.currentLocation())

if __name__ == '__main__':
    unittest.main()

