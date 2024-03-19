class Plateau:
    def __init__(self, top_right_x_coordinate, top_right_y_coordinate):
        self.top_right_coordinates = Coordinates(0, 0)
        self.bottom_left_coordinates = Coordinates(0, 0)
        self.top_right_coordinates = self.top_right_coordinates.new_coordinates_for(top_right_x_coordinate, top_right_y_coordinate)
    
    def has_within_bounds(self, coordinates):
        return self.bottom_left_coordinates.has_outside_bounds(coordinates) and self.top_right_coordinates.has_within_bounds(coordinates)