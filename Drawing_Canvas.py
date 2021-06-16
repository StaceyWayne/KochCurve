import tkinter as tk
from wedge_piece_class import one_point

class Canvas_Class(tk.Canvas):
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        
        self.main_dlg = args[0]

        self.grid(row=1, column=2, sticky='nsew')
        self.config(bg='white')
        self.grid_propagate(0)

        self.scale_factor_x = 1
        self.scale_factor_y = 1
        self.translate_x = 0
        self.translate_y = 0

    def set_scale(self, max_x, min_x, max_y, min_y):
        window_max_x = self.winfo_width()
        window_max_y = self.winfo_height()
        window_min_x = 0
        window_min_y = 0

        self.scale_factor_x = (window_max_x - window_min_x)/(max_x-min_x)
        self.scale_factor_y = (window_max_y - window_min_y) / (max_y - min_y)

        self.translate_x = self.scale_factor_x*min_x-window_min_x
        self.translate_y = self.scale_factor_y  * min_y - window_min_y

    def draw_line(self, start, end):
        temp = start.x * self.scale_factor_x - self.translate_x
        temp = start.y*self.scale_factor_y - self.translate_y
        temp =  end.x * self.scale_factor_x - self.translate_x
        temp = end.y * self.scale_factor_y - self.translate_y
        self.create_line(start.x*self.scale_factor_x-self.translate_x,
                         start.y*self.scale_factor_y-self.translate_y,
                         end.x * self.scale_factor_x - self.translate_x,
                         end.y * self.scale_factor_y - self.translate_y)
        # max_x = self.winfo_width()
        # max_y = self.winfo_height()
        # x = []
        # y = []
        # x.append(1)
        # x.append(-1)
        # x.append(0)
        # y.append(-1)
        # y.append(-1)
        # y.append(3**(1/2)-1)
        #
        # x.append(0)
        # x.append(-1)
        # x.append(1)
        #
        # y.append(-1.5777)
        # y.append(.1547)
        # y.append(.1547)
        #
        # for index in range(6):
        #     x[index] = (x[index] + 2) * max_x/4
        #     y[index] = (y[index] + 2) * max_y/4
        #
        #
        # self.create_line(x[0], y[0], x[1], y[1])
        # self.create_line(x[1], y[1], x[2], y[2])
        # self.create_line(x[2], y[2], x[0], y[0])
        # self.create_line(x[3], y[3], x[4], y[4])
        # self.create_line(x[4], y[4], x[5], y[5])
        # self.create_line(x[5], y[5], x[3], y[3])


