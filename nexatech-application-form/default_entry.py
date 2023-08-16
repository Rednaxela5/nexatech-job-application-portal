import tkinter as tk

class DefaultTextEntry(tk.Entry):
    def __init__(self, master=None, default_text='', default_text_color='grey', *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.default_text = default_text
        self.default_text_color = default_text_color
        self.set_default_text()
        self.get()
        self.bind('<FocusIn>', self.on_entry_click)
        self.bind('<FocusOut>', self.on_focus_out)

    def set_default_text(self):
        """Set the default text and color when the widget is created."""
        self.insert(0, self.default_text)
        self.config(fg=self.default_text_color)

    # def load_current(self):
    def on_entry_click(self, event):
        """Function to handle the event when the Entry box is clicked."""
        
        if self.get() == 'Enter Password': # For Password
            self.delete(0, tk.END)
            self.config(fg='black', show='•', font="Monserratbold")
        elif self.get() == self.default_text:
            self.delete(0, tk.END)
            self.config(fg='black')

    def on_focus_out(self, event):
        """Function to handle the event when the Entry box loses focus."""
        if self.get() == '' and self.default_text == 'Enter Password': # For Password
            self.config(show='', font="Montserrat")
            self.default_text = 'Enter Password'
            self.set_default_text()
        elif self.get() == '':
            self.set_default_text()
       