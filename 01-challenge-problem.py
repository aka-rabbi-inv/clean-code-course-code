class Point:
    def __init__(self, x, y):
        self.x_coordinate = x
        self.y_coordinate = y


class Rectangle:
    def __init__(self, starting_point, length, width):
        self.starting_point = starting_point
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

    def print_end_point_coordinates(self):
        top_right = self.starting_point.x + self.length
        bottom_left = self.starting_point.y + self.width
        print('Starting Point (X)): ' + str(self.starting_point.x))
        print('Starting Point (Y)): ' + str(self.starting_point.y))
        print('End Point X-Axis (Top Right): ' + str(top_right))
        print('End Point Y-Axis (Bottom Left): ' + str(bottom_left))


def construct_rectangle():
    starting_point = Point(50, 100)
    return Rectangle(starting_point, 90, 10)


my_rectangle = construct_rectangle()

print(my_rectangle.get_area())
my_rect.print_end_point_coordinates()
