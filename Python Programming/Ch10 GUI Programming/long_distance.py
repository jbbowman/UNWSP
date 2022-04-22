# This program demonstrates a group of Radiobutton widgets.

import tkinter
import tkinter.messagebox


class MyGUI:
    def __init__(self):
        # Create the main window.
        self.main_window = tkinter.Tk()

        # Create two frames. One for the Radiobuttons
        # and another for the regular Button widgets.
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Create an IntVar object to use with
        # the Radiobuttons.
        self.radio_var = tkinter.IntVar()

        # Set the intVar object to 1.
        self.radio_var.set(1)

        # Create the Radiobutton widgets in the top_frame.
        self.rb1 = tkinter.Radiobutton(self.top_frame,
                                       text='Daytime (6:00 - 17:59)',
                                       variable=self.radio_var,
                                       value=1)
        self.rb2 = tkinter.Radiobutton(self.top_frame,
                                       text='Evening (18:00 - 23:59)',
                                       variable=self.radio_var,
                                       value=2)
        self.rb3 = tkinter.Radiobutton(self.top_frame,
                                       text='Off-peak (0:00 - 5:59)',
                                       variable=self.radio_var,
                                       value=3)

        # Pack the Radiobuttons.
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        self.label = tkinter.Label(self.bottom_frame, text='Minutes:')
        self.eb1 = tkinter.Entry(self.bottom_frame)

        self.label.pack()
        self.eb1.pack()

        # Create an OK button and a Quit button.
        self.display_button = tkinter.Button(self.bottom_frame,
                                        text='Display Changes',
                                        command=self.show_choice)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Quit',
                                          command=self.main_window.destroy)

        # Pack the Buttons.
        self.display_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack the frames.
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Start the mainloop.
        tkinter.mainloop()

    # The show_choice method is the callback function for the
    # OK button.

    def show_choice(self):
        charge = 0

        if self.radio_var.get() == 1:
            charge = 0.10
            tkinter.messagebox.showinfo('Total Charges', 'Your total charge = $' +
                                        str(charge * float(self.eb1.get())))
        elif self.radio_var.get() == 2:
            charge = 0.15
            tkinter.messagebox.showinfo('Total Charges', 'Your total charge = $' +
                                        str(charge * float(self.eb1.get())))
        elif self.radio_var.get() == 3:
            charge = 0.05
            tkinter.messagebox.showinfo('Total Charges', 'Your total charge = $' +
                                        str(charge * float(self.eb1.get())))

# Create an instance of the MainWindow class.
if __name__ == '__main__':
    my_gui = MyGUI()