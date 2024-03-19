

from assiegnment.rover.commands import ICommand
from assiegnment.rover.parser import StringCommandParser
from assiegnment.rover.universe import Coordinates, Direction, Plateau

class MarsRover:
    def __init__(self, plateau, direction, coordinates):
        self.plateau = plateau
        self.currentDirection = direction
        self.currentCoordinates = coordinates

    def run(self, commandString):
        roverCommands = StringCommandParser(commandString).toCommands()
        for command in roverCommands:
            command.execute(self)

    def currentLocation(self):
        return str(self.currentCoordinates) + " " + str(self.currentDirection)

    def turnRight(self):
        self.currentDirection = self.currentDirection.right()

    def turnLeft(self):
        self.currentDirection = self.currentDirection.left()

    def move(self):
        positionAfterMove = self.currentCoordinates.newCoordinatesForStepSize(self.currentDirection.stepSizeForXAxis(), self.currentDirection.stepSizeForYAxis())

        # ignores the command if rover is being driven off plateau
        if self.plateau.hasWithinBounds(positionAfterMove):
            self.currentCoordinates = self.currentCoordinates.newCoordinatesFor(self.currentDirection.stepSizeForXAxis(), self.currentDirection.stepSizeForYAxis())