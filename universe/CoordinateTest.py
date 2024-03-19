import unittest
from assiegnment.rover.universe import Coordinates

class CoordinateTest(unittest.TestCase):

    def test_x_coordinates_are_incremented_for_positive_value(self):
        # Given
        boundary_coordinates = Coordinates(2, 3)

        # When
        boundary_coordinates = boundary_coordinates.new_coordinates_for(1, 0)

        # Then
        self.assertEqual("3 3", str(boundary_coordinates))

    def test_x_coordinates_are_decremented_for_negative_value(self):
        # Given
        boundary_coordinates = Coordinates(2, 3)

        # When
        boundary_coordinates = boundary_coordinates.new_coordinates_for(-1, 0)

        # Then
        self.assertEqual("1 3", str(boundary_coordinates))

    def test_y_coordinates_are_incremented_for_positive_value(self):
        # Given
        boundary_coordinates = Coordinates(2, 3)

        # When
        boundary_coordinates = boundary_coordinates.new_coordinates_for(0, 1)

        # Then
        self.assertEqual("2 4", str(boundary_coordinates))

    def test_y_coordinates_are_decremented_for_negative_value(self):
        # Given
        boundary_coordinates = Coordinates(2, 3)

        # When
        boundary_coordinates = boundary_coordinates.new_coordinates_for(0, -1)

        # Then
        self.assertEqual("2 2", str(boundary_coordinates))

    def test_point_with_x_coordinate_within_boundary_are_identified(self):
        # Given
        boundary_coordinates = Coordinates(5, 5)

        # When
        internal_point = Coordinates(4, 5)

        # Then
        self.assertTrue(boundary_coordinates.has_within_bounds(internal_point))

    def test_point_with_y_coordinate_within_boundary_are_identified(self):
        # Given
        boundary_coordinates = Coordinates(5, 5)

        # When
        internal_point = Coordinates(5, 4)

        # Then
        self.assertTrue(boundary_coordinates.has_within_bounds(internal_point))

    def test_points_with_x_coordinate_outside_boundary_are_identified(self):
        # Given
        boundary_coordinates = Coordinates(5, 5)

        # When
        external_point = Coordinates(8, 5)

        # Then
        self.assertTrue(boundary_coordinates.has_outside_bounds(external_point))

    def test_points_with_y_coordinate_outside_boundary_are_identified(self):
        # Given
        boundary_coordinates = Coordinates(5, 5)

        # When
        external_point = Coordinates(5, 8)

        # Then
        self.assertTrue(boundary_coordinates.has_outside_bounds(external_point))

    def test_immutable_coordinates_are_created_for_new_step_size(self):
        # Given
        boundary_coordinates = Coordinates(5, 5)

        # When
        new_boundary = boundary_coordinates.new_coordinates_for_step_size(1, -1)

        # Then
        self.assertEqual("6 4", str(new_boundary))
        self.assertEqual("5 5", str(boundary_coordinates))