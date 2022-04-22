# This program gets the user's selection from a Listbox.
import tkinter
import tkinter.messagebox

class ListBoxSelection:
    def __init__(self):
        # Create the main window.
        self.main_window = tkinter.Tk()

        # Create a Listbox widget.
        self.language_listbox = tkinter.Listbox(
            self.main_window, width=0, height=0)
        self.language_listbox.pack(padx=10, pady=5)

        # Create a list with the names of languages.
        languages = ['C', 'C++', 'Java', 'Python']

        # Populate the Listbox with the list contents.
        for language in languages:
            self.language_listbox.insert(tkinter.END, language)

        # Create a button to get the selected item.
        self.get_button = tkinter.Button(
            self.main_window, text='Get Item',
            command=self.__retrieve_language)
        self.get_button.pack(padx=10, pady=5)

        self.delete_button = tkinter.Button(
            self.main_window, text='Delete Item',
            command=self.__delete_item)
        self.delete_button.pack(padx=10, pady=5)

        self.quit_button = tkinter.Button(self.main_window, text= 'Quit', command=self.main_window.destroy)
        self.quit_button.pack(padx=10, pady=5)

        # Start the main loop.
        tkinter.mainloop()

    def __retrieve_language(self):
        # Get the index of the selected item.
        indexes = self.language_listbox.curselection()

        # If an item is selected, display it.
        if len(indexes) > 0:
            tkinter.messagebox.showinfo(
                message=self.language_listbox.get(indexes[0]))
        else:
            tkinter.messagebox.showinfo(
                message='No item selected.')

    def __delete_item(self):
        indexes = self.language_listbox.curselection()

        if len(indexes) > 0:
            self.language_listbox.delete(indexes[0], last=None)
            tkinter.messagebox.showinfo(
                message='Item has been deleted.')
        else:
            tkinter.messagebox.showinfo(
                message='No item selected.')

# Create an instance of the ListBoxSelection class.
if __name__ == '__main__':
    listbox_selection = ListBoxSelection()