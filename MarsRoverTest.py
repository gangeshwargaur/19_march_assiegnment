from assiegnment.rover.MarsRover import MarsRover
from assiegnment.rover.universe.Coordinates import Coordinates
from assiegnment.rover.universe.Direction import Direction
from assiegnment.rover.universe.Plateau import Plateau
import unittest

class MarsRoverTest(unittest.TestCase):
    def test_canProvideCurrentLocationAsString(self):
        plateau = Plateau(5, 5)
        startingPosition = Coordinates(1, 2)
        marsRover = MarsRover(plateau, Direction.N, startingPosition)
        self.assertEqual("1 2 N", marsRover.currentLocation())


    def test_canMove(self):
        plateau = Plateau(5, 5)
        startingPosition = Coordinates(1, 2)
        marsRover = MarsRover(plateau, Direction.N, startingPosition)
        marsRover.move()
        self.assertEqual("1 3 N", marsRover.currentLocation())


    def test_canRunCommandToMove(self):
        plateau = Plateau(5, 5)
        startingPosition = Coordinates(1, 2)
        marsRover = MarsRover(plateau, Direction.N, startingPosition)
        marsRover.run("M")
        self.assertEqual("1 3 N", marsRover.currentLocation())



if __name__ == '__main__':
    unittest.main()

