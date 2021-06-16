from wedge_piece_class import Wedge_Piece_Class
from wedge_piece_class import one_point


class the_curve_class():
    def __init__(self):

        self.the_pieces = []
                                # this is where the individual pieces will be
                                # the first index is the iteration
                                # the second index will be the object of one wedge piece
        self.which_iteration = -1

    def next_iteration(self):
        if self.which_iteration==-1:
            a = one_point(1, -1)
            b = one_point(-1, -1)
            c = one_point(0, ((3 ** 0.5) - 1))

            temp_array = []
            temp_array.append(Wedge_Piece_Class(a, b))
            temp_array.append(Wedge_Piece_Class(b, c))
            temp_array.append(Wedge_Piece_Class(c, a))

            self.the_pieces.append(temp_array)
            self.which_iteration = self.which_iteration + 1

        else:
            the_points = self.get_points()
            temp_array = []

            for index in range(len(the_points)-1):
                temp_array.append(Wedge_Piece_Class(the_points[index], the_points[index+1]))

            temp_array.append(Wedge_Piece_Class(the_points[len(the_points)-1], the_points[0]))
            self.which_iteration = self.which_iteration + 1
            self.the_pieces.append(temp_array)

    def get_max_y(self):

        return_value = 0
        for one_wedge in self.the_pieces[self.which_iteration]:
            return_value = max(return_value, one_wedge.get_max_y())

        return return_value

    def get_max_x(self):

        return_value = 0
        for one_wedge in self.the_pieces[self.which_iteration]:
            return_value = max(return_value, one_wedge.get_max_x())

        return return_value

    def get_min_y(self):

        return_value = 0
        for one_wedge in self.the_pieces[self.which_iteration]:
            return_value = min(return_value, one_wedge.get_min_y())

        return return_value

    def get_min_x(self):

        return_value = 0
        for one_wedge in self.the_pieces[self.which_iteration]:
            return_value = min(return_value, one_wedge.get_min_x())

        return return_value

    def get_points(self):
        return_value = []

        for this_wedge in self.the_pieces[self.which_iteration]:
            return_value.append(this_wedge.point_a)
            return_value.append(this_wedge.point_b)
            return_value.append(this_wedge.point_c)
            return_value.append(this_wedge.point_d)

        return return_value

    def remove_last_iteration(self):
        del self.the_pieces[len(self.the_pieces)-1]
        self.which_iteration = self.which_iteration - 1

    def calculate_perimeter(self):
        return_value = 0

        for this_wedge in self.the_pieces[self.which_iteration]:
            return_value = return_value + this_wedge.calculate_wedge_length()

        return return_value