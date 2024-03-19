class Coordinates:
    def __init__(self, xCoordinate, yCoordinate):
        self.xCoordinate = xCoordinate
        self.yCoordinate = yCoordinate

    def newCoordinatesFor(self, xCoordinateStepValue, yCoordinateStepValue):
        return Coordinates(self.xCoordinate + xCoordinateStepValue, self.yCoordinate + yCoordinateStepValue)

    def __str__(self):
        return str(self.xCoordinate) + " " + str(self.yCoordinate)

    def hasWithinBounds(self, coordinates):
        return self.isXCoordinateWithinBounds(coordinates.xCoordinate) and self.isYCoordinateWithinBounds(coordinates.yCoordinate)

    def hasOutsideBounds(self, coordinates):
        return self.isXCoordinateInOutsideBounds(coordinates.xCoordinate) and self.isYCoordinateInOutsideBounds(coordinates.yCoordinate)

    def isXCoordinateInOutsideBounds(self, xCoordinate):
        return xCoordinate >= self.xCoordinate

    def isYCoordinateInOutsideBounds(self, yCoordinate):
        return yCoordinate >= self.yCoordinate

    def isYCoordinateWithinBounds(self, yCoordinate):
        return yCoordinate <= self.yCoordinate

    def isXCoordinateWithinBounds(self, xCoordinate):
        return xCoordinate <= self.xCoordinate

    def newCoordinatesForStepSize(self, xCoordinateStepValue, yCoordinateStepValue):
        return Coordinates(self.xCoordinate + xCoordinateStepValue, self.yCoordinate + yCoordinateStepValue)

