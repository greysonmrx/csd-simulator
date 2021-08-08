from tkinter import ttk

class LogicalPorts():
    def __init__(self, frame=None):
        self.frame = frame
        self.setup()

    def setup(self):
        # Setting up all elements of the screen

        ttk.Label(self.frame, text='Logical Ports screen!').grid(column=0, row=0, padx=30, pady=30)