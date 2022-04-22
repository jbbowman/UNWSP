# This program demonstrates a group of Checkbutton widgets.
import tkinter
import tkinter.messagebox

class MainWindow:
    def __init__(self):
        # create root window
        self.root = tkinter.Tk()

        # create frames
        self.top_frame = tkinter.Frame(self.root)
        self.bottom_frame = tkinter.Frame(self.root)

        # create costs constants and total variable
        self.OIL_CHANGE = 49.99
        self.TIRE_ROTATION = 39.99
        self.ALIGNMENT = 44.95
        self.total = 0

        # create variables for buttons/label
        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()
        self.l1_var1 = tkinter.StringVar()

        # set variables
        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)
        self.l1_var1.set(f'Total Cost: {self.total}')

        # create 3 check buttons and 1 label
        self.cb1 = tkinter.Checkbutton(self.top_frame, text='Oil Change', variable=self.cb_var1, command=self.add_cost)
        self.cb2 = tkinter.Checkbutton(self.top_frame, text='Tire Rotation', variable=self.cb_var2, command=self.add_cost)
        self.cb3 = tkinter.Checkbutton(self.top_frame, text='Alignment', variable=self.cb_var3, command=self.add_cost)
        self.l1 = tkinter.Label(self.top_frame, textvariable=self.l1_var1)

        # pack buttons/label
        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()
        self.l1.pack()

        # create quit button
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.root.destroy)

        # Pack the quit button.
        self.quit_button.pack(side='left')

        # Pack the frames.
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Start the mainloop.
        tkinter.mainloop()

    def add_cost(self):  # logic statements to calculate total variable
        if self.cb_var1.get() == 0:
            self.total = 0
        if self.cb_var2.get() == 0:
            self.total = 0
        if self.cb_var3.get() == 0:
            self.total = 0
        if self.cb_var1.get() == 1:
            self.total += self.OIL_CHANGE
        if self.cb_var2.get() == 1:
            self.total += self.TIRE_ROTATION
        if self.cb_var3.get() == 1:
            self.total += self.ALIGNMENT
        if self.cb_var1.get() == 1 and self.cb_var2.get() == 1 and self.cb_var3.get() == 1:
            self.total = self.OIL_CHANGE + self.TIRE_ROTATION + self.ALIGNMENT

        self.l1_var1.set(f'Total Cost: {self.total}')


if __name__ == '__main__':
    MainWindow()
