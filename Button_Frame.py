import tkinter as tk


class Button_Frame_Class( tk.Frame):
    def __init__(self, the_curve, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.the_curve = the_curve

        self.main_dlg = args[0]
        
        self.grid(row=1, column=1, sticky='nsew')
        self.config(bg='red')
        self.grid_propagate(0)
        
        this_row = 0
        self.rowconfigure(this_row, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(3, weight=1)

        this_row = this_row + 1
        one_lable = tk.Label(self, text='This is where your interface will be')
        one_lable.config(bg='red')
        one_lable.grid(row=this_row, column=1)

        this_row = this_row + 1
        next_iteration_button = tk.Button(self, text='Next Iteration', command=self.next_iteration)
        next_iteration_button.grid(row=this_row, column=1)

        this_row = this_row + 1
        previous_iteration_button = tk.Button(self, text='Previous Iteration', name='previous_iteration_button', command=self.previous_iteration)
        previous_iteration_button.grid(row=this_row, column=1)
        previous_iteration_button.config(state='disable')

        this_row = this_row + 1
        calculate_perimeter_button = tk.Button(self, text='Calculate Perimeter', name='calculate_perimeter_button', command=self.calculate_perimeter)
        calculate_perimeter_button.grid(row=this_row, column=1)

        tk.Label(self, text='', name='perimeter_label', bg='red').grid(row=this_row, column=2)

        this_row = this_row + 1
        self.rowconfigure(this_row, weight=1)

    def calculate_perimeter(self):
        self.nametowidget('perimeter_label').config(text='Perimeter = ' + str(self.the_curve.calculate_perimeter()))

    def draw_current_iteration(self):
        drawing_area = self.main_dlg.nametowidget('our_canvas')
        drawing_area.delete('all')

        drawing_area.set_scale(self.the_curve.get_max_x()+.25, self.the_curve.get_min_x()-.25, self.the_curve.get_max_y()+.25, self.the_curve.get_min_y()-.25)
        the_points = self.the_curve.get_points()

        for index in range(len(the_points)-1):
            drawing_area.draw_line(the_points[index], the_points[index+1])

        drawing_area.draw_line(the_points[len(the_points)-1], the_points[0])

    def next_iteration(self):
        self.the_curve.next_iteration()
        self.draw_current_iteration()
        self.nametowidget('previous_iteration_button').config(state='normal')

    def previous_iteration(self):
        self.the_curve.remove_last_iteration()


        if self.the_curve.which_iteration == -1:
            self.nametowidget('previous_iteration_button').config(state='disable')
            drawing_area = self.main_dlg.nametowidget('our_canvas').delete('all')
        else:
            self.draw_current_iteration()
