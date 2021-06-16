class one_point():
    def __init__(self,x,y):
        self.x=x
        self.y=y

class Wedge_Piece_Class():
    def __init__(self, point_a, point_e):
        
        # for each iteration we will be making a new Wedge Piece for each line segment
        # point_a and point_e are the end points of the line segments

        self.point_a = point_a
        self.point_e = point_e
        
        self.calculate_point_b()

        self.calculate_point_d()
        self.point_c = one_point(0,0)

        self.calculate_point_c()

    def get_max_x(self):
        return max(self.point_a.x, self.point_b.x, self.point_c.x, self.point_d.x, self.point_e.x)

    def get_min_x(self):
        return min(self.point_a.x, self.point_b.x, self.point_c.x, self.point_d.x, self.point_e.x)

    def get_max_y(self):
        return max(self.point_a.y, self.point_b.y, self.point_c.y, self.point_d.y, self.point_e.y)

    def get_min_y(self):
        return min(self.point_a.y, self.point_b.y, self.point_c.y, self.point_d.y, self.point_e.y)

    def new_point(self, start_point, end_point, fractional_distance):
        return one_point(start_point.x + fractional_distance * (end_point.x-start_point.x),start_point.y + fractional_distance * (end_point.y - start_point.y))


    def calculate_point_b(self):
        self.point_b = self.new_point(self.point_a, self.point_e, 1/3)

    def distance_betweeen_two_points(self, start, end):
        return ((start.x-end.x)**2 + (start.y-end.y)**2)**(1/2)

    def calculate_point_c(self):
        #
        # temp_b = one_point(self.point_b.x, self.point_b.y)
        #
        # self.translate_by_z(temp_b)
        #
        # m = self.new_point(self.point_b, self.point_d, 1/2)
        #
        # hypotenuse = self.distance_betweeen_two_points(m, self.point_b)
        # cos_theta = (m.x-self.point_b.x)/hypotenuse
        # sin_theta = -(m.y-self.point_b.y)/hypotenuse
        #
        # self.rotate_by_theta(cos_theta, sin_theta)
        # m = self.rotate_this_point_by_theta(cos_theta, sin_theta, m)
        # self.point_c.x = m.x
        # self.point_c.y = m.y + hypotenuse * (3**(1/2))
        #
        # self.rotate_by_theta(cos_theta, -1*sin_theta)
        #
        # temp_b.x = temp_b.x * -1
        # temp_b.y = temp_b.y * -1
        # self.translate_by_z(temp_b)

        temp_b = one_point(self.point_b.x, self.point_b.y)

        self.translate_by_z(temp_b)



        hypotenuse = self.distance_betweeen_two_points(self.point_d, self.point_b)
        cos_theta = (self.point_d.x-self.point_b.x)/hypotenuse
        sin_theta = -(self.point_d.y-self.point_b.y)/hypotenuse

        self.rotate_by_theta(cos_theta, sin_theta)
        m = self.new_point(self.point_b, self.point_d, 1/2)

        self.point_c.x = m.x
        self.point_c.y = m.y + hypotenuse * (3**(1/2)) * 0.5

        self.rotate_by_theta(cos_theta, -1*sin_theta)

        temp_b.x = temp_b.x * -1
        temp_b.y = temp_b.y * -1
        self.translate_by_z(temp_b)

    def calculate_point_d(self):
        self.point_d = self.new_point(self.point_a, self.point_e, 2/3)

    def rotate_this_point_by_theta(self, cos_theta, sin_theta, this_point):
        old_x = this_point.x
        this_point.x = this_point.x * cos_theta - this_point.y * sin_theta
        this_point.y = old_x * sin_theta + this_point.y * cos_theta
        return this_point

    def rotate_by_theta(self, cos_theta, sin_theta):
        # old_x = self.point_a.x
        # self.point_a.x = self.point_a.x * cos_theta - self.point_a.y * sin_theta
        # self.point_a.y = old_x * sin_theta + self.point_a.y * cos_theta

        old_x = self.point_b.x
        self.point_b.x = self.point_b.x * cos_theta - self.point_b.y * sin_theta
        self.point_b.y = old_x * sin_theta + self.point_b.y * cos_theta

        old_x = self.point_c.x
        self.point_c.x = self.point_c.x * cos_theta - self.point_c.y * sin_theta
        self.point_c.y = old_x * sin_theta + self.point_c.y * cos_theta

        old_x = self.point_d.x
        self.point_d.x = self.point_d.x * cos_theta - self.point_d.y * sin_theta
        self.point_d.y = old_x * sin_theta + self.point_d.y * cos_theta

        # old_x = self.point_e.x
        # self.point_e.x = self.point_e.x * cos_theta - self.point_e.y * sin_theta
        # self.point_e.y = old_x * sin_theta + self.point_e.y * cos_theta

    def translate_by_z(self, z):
        
        # self.point_a.x = self.point_a.x - z.x
        self.point_b.x = self.point_b.x - z.x
        self.point_c.x = self.point_c.x - z.x
        self.point_d.x = self.point_d.x - z.x
        # self.point_e.x = self.point_e.x - z.x
        
        # self.point_a.y = self.point_a.y - z.y
        self.point_b.y = self.point_b.y - z.y
        self.point_c.y = self.point_c.y - z.y
        self.point_d.y = self.point_d.y - z.y
        # self.point_e.y = self.point_e.y - z.y

    def calculate_wedge_length(self):
        return_value = 0
        return_value = return_value + self.distance_betweeen_two_points(self.point_a, self.point_b)
        return_value = return_value + self.distance_betweeen_two_points(self.point_b, self.point_c)
        return_value = return_value + self.distance_betweeen_two_points(self.point_c, self.point_d)
        return_value = return_value + self.distance_betweeen_two_points(self.point_d, self.point_e)
        return return_value