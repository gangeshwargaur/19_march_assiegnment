# Framework and Technology Stack: JUnit, ThoughtWorks Rover

from assiegnment.rover.universe import Coordinates
from assiegnment.rover.universe import Plateau
import unittest

class PlateauTest(unittest.TestCase):

    def test_location_with_coordinate_within_bounds_is_identified(self):
        # Given
        mars = Plateau(5, 5)

        # When
        plateau_coordinates = Coordinates(5, 0)

        # Then
        self.assertTrue(mars.has_within_bounds(plateau_coordinates))

    def test_location_with_positive_x_coordinate_outside_bounds_is_identified(self):
        # Given
        mars = Plateau(5, 5)

        # When
        coordinates = Coordinates(6, 0)

        # Then
        self.assertFalse(mars.has_within_bounds(coordinates))

    def test_location_with_negative_x_coordinate_outside_bounds_is_identified(self):
        # Given
        mars = Plateau(5, 5)

        # When
        coordinates = Coordinates(-1, 0)

        # Then
        self.assertFalse(mars.has_within_bounds(coordinates))

    def test_location_with_positive_y_coordinate_outside_bounds_is_identified(self):
        # Given
        mars = Plateau(5, 5)

        # When
        coordinates = Coordinates(0, 6)

        # Then
        self.assertFalse(mars.has_within_bounds(coordinates))

    def test_location_with_negative_y_coordinate_outside_bounds_is_identified(self):
        # Given
        mars = Plateau(5, 5)

        # When
        coordinates = Coordinates(0, -1)

        # Then
        self.assertFalse(mars.has_within_bounds(coordinates))