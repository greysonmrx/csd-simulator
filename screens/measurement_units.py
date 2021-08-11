from tkinter import ttk
from tkinter.constants import X
from tkinter.font import NORMAL, BOLD, Font


class MeasurementUnits:
    def __init__(self, frame=None):
        self.frame = frame
        self.measurement_units = ["Binário", "Octal", "Decimal", "Hexadecimal"]
        self.setup()

    def setup(self):
        container = ttk.Frame(self.frame)
        container.pack(fill=X, padx=30, pady=30)

        ttk.Label(
            container,
            text="Unidades de medida",
            font=Font(container, size=20, weight=BOLD),
        ).pack()

        ttk.Label(
            container,
            text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse elementum lobortis nulla sit amet suscipit. Proin consequat sem eget imperdiet viverra.",
            font=Font(container, size=11, weight=NORMAL),
            justify="center",
            wraplength=500,
            anchor="center",
        ).pack(pady=[8, 30])

        operation = ttk.Labelframe(
            container, text="Operação", borderwidth=2, relief="solid"
        )
        operation.pack(fill=X, ipady=9)

        ttk.Label(operation, text="Converter").grid(
            column=0, row=0, sticky="w", padx=18, pady=[10, 2]
        )
        self.value = ttk.Entry(operation, width=22)
        self.value.grid(column=0, row=1, padx=18)

        ttk.Label(operation, text="De").grid(column=1, row=0, sticky="w", pady=[10, 2])
        self.first_measurement_unit = ttk.Combobox(
            operation, values=self.measurement_units, width=22
        )
        self.first_measurement_unit.set("Binário")
        self.first_measurement_unit.grid(column=1, row=1)

        ttk.Label(operation, text="Para").grid(
            column=2, row=0, sticky="w", padx=18, pady=[10, 2]
        )
        self.second_measurement_unit = ttk.Combobox(
            operation, values=self.measurement_units, width=22
        )
        self.second_measurement_unit.set("Binário")
        self.second_measurement_unit.grid(column=2, row=1, padx=18)

        ttk.Button(operation, text="Converter", command=self.execute_operation).grid(
            column=2, row=2, pady=[18, 0], padx=18, sticky="e"
        )

        self.result = ttk.Label(
            container, text="Resultado: 30", font=Font(container, size=13, weight=BOLD)
        ).pack(pady=30)

    def execute_operation(self):
        print(
            "Execute code to convert {} from {} to {}".format(
                self.value.get(),
                self.first_measurement_unit.get(),
                self.second_measurement_unit.get(),
            )
        )
