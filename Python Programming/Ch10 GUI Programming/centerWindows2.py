from tkinter import *

def center_window(w=500,h=500):
    # get screen width and height
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()

    # calculate position x, y
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    root.geometry('+%d+%d' %  (x,y))

root = Tk()
center_window(500,300)
root.mainloop()


