import tkinter
from tkinter import ttk

from screens.about import About
from screens.relational_algebra import RelationalAlgebra
from screens.logical_ports import LogicalPorts
from screens.sum_of_binaries import SumOfBinaries
from screens.number_systems import NumberSystems
from screens.measurement_units import MeasurementUnits

class Application(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

    def start(self):
        self.pack()
        self.setup()
        self.mainloop()

    def setup(self):
        self.render_tabs()
        self.set_title('Projeto AB1')

    def set_title(self, title=''):
        self.master.title(title)

    def render_tabs(self):
        tab_control = ttk.Notebook(self.master)

        opa = ttk.Frame(tab_control)

        tabs = [
            {
                'name': 'Unidades de medida',
                'frame': opa,
                'screen': MeasurementUnits
            },
            {
                'name': 'Bases numéricas',
                'frame': ttk.Frame(tab_control),
                'screen': NumberSystems
            },
            {
                'name': 'Soma de binários',
                'frame': ttk.Frame(tab_control),
                'screen': SumOfBinaries
            },
            {
                'name': 'Portas lógicas',
                'frame': ttk.Frame(tab_control),
                'screen': LogicalPorts
            },
            {
                'name': 'Álgebra relacional',
                'frame': ttk.Frame(tab_control),
                'screen': RelationalAlgebra
            },
            {
                'name': 'Sobre o projeto',
                'frame': ttk.Frame(tab_control),
                'screen': About
            }
        ]

        for tab in tabs:
            tab_control.add(tab['frame'], text=tab['name'])

            tab['screen'](tab['frame'])


        tab_control.pack(expand=1, fill="both")

app = Application(master=tkinter.Tk())
app.start()
