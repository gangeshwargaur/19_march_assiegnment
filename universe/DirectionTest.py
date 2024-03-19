import unittest
from assiegnment.rover.universe.Direction import Direction

class DirectionTest(unittest.TestCase):

    def test_west_is_on_left_of_north(self):
        # Given
        north = Direction.N

        # When
        west = north.left()

        # Then
        self.assertEqual(Direction.W, west)

    def test_east_is_on_right_of_north(self):
        # Given
        north = Direction.N

        # When
        east = north.right()

        # Then
        self.assertEqual(Direction.E, east)

    def test_north_is_on_right_of_west(self):
        # Given
        west = Direction.W

        # When
        north = west.right()

        # Then
        self.assertEqual(Direction.N, north)

    def test_south_is_on_left_of_west(self):
        # Given
        west = Direction.W

        # When
        south = west.left()

        # Then
        self.assertEqual(Direction.S, south)

    def test_east_is_on_left_of_south(self):
        # Given
        south = Direction.S

        # When
        east = south.left()

        # Then
        self.assertEqual(Direction.E, east)

    def test_west_is_on_right_of_south(self):
        # Given
        south = Direction.S

        # When
        west = south.right()

        # Then
        self.assertEqual(Direction.W, west)

    def test_north_is_on_left_of_east(self):
        # Given
        east = Direction.E

        # When
        north = east.left()

        # Then
        self.assertEqual(Direction.N, north)

    def test_south_is_on_right_of_east(self):
        # Given
        east = Direction.E

        # When
        south = east.right()

        # Then
        self.assertEqual(Direction.S, south)

    def test_east_is_one_step_forward_on_x_axis(self):
        # Given
        east = Direction.E

        # When
        step_size = east.stepSizeForXAxis()

        # Then
        self.assertEqual(1, step_size)

    def test_east_is_stationary_on_y_axis(self):
        # Given
        east = Direction.E

        # When
        step_size = east.stepSizeForYAxis()

        # Then
        self.assertEqual(0, step_size)

    def test_west_is_one_step_back_on_x_axis(self):
        # Given
        west = Direction.W

        # When
        step_size = west.stepSizeForXAxis()

        # Then
        self.assertEqual(-1, step_size)

    def test_west_is_stationary_on_y_axis(self):
        # Given
        west = Direction.W

        # When
        step_size = west.stepSizeForYAxis()

        # Then
        self.assertEqual(0, step_size)

    def test_north_is_one_step_forward_on_y_axis(self):
        # Given
        north = Direction.N

        # When
        step_size = north.stepSizeForYAxis()

        # Then
        self.assertEqual(1, step_size)

    def test_north_is_stationary_on_x_axis(self):
        # Given
        north = Direction.N

        # When
        step_size = north.stepSizeForXAxis()

        # Then
        self.assertEqual(0, step_size)

    def test_south_is_one_step_back_on_y_axis(self):
        # Given
        south = Direction.S

        # When
        step_size = south.stepSizeForYAxis()

        # Then
        self.assertEqual(-1, step_size)

    def test_south_is_stationary_on_x_axis(self):
        # Given
        south = Direction.S

        # When
        step_size = south.stepSizeForXAxis()

        # Then
        self.assertEqual(0, step_size)