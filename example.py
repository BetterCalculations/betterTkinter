import tkinter as tk  # Import GUI
import tk_place as place  # This is very long to pls use from tk_place import *

# please use this class structure for tkinter GUI's


class App(tk.Tk):
    def __init__(self, app_width: int, app_height: int):
        super().__init__()
        self.DARKMODE_TXT = "🌙"
        self.WHITEMODE_TXT = "☀"
        self.title("Example better placer")
        self.resizable(False, False)
        self.BIG = 20
        self.isDarkMode = False
        self.components = []
        self.MEDIUM = 15
        self.SMALL = 12
        self.BLACK = "#000"
        self.WHITE = "#fff"
        self.DARKMODE_COLOR = "#252525"
        self.app_width = app_width
        self.app_height = app_height
        self.geometry(f"{self.app_width}x{self.app_height}")
        self.calc = place.Placer(self.app_width, self.app_height)
        self.label_example = tk.Label(self, text="Example Caption", font=("Arial", self.BIG, "bold"))
        self.label_example.place(x=self.calc.get_width(self.calc.top_center()), y=self.calc.get_height(self.calc.top_center(0)))
        self.button_example = tk.Button(self, bd=0, text="🌙", font=("Arial", 20, "bold"), command=self.set_theme)
        self.button_example.place(x=self.calc.get_width(self.calc.top_left(0)), y=self.calc.get_height(self.calc.top_left(0)))
        self.listbox_example = tk.Listbox(self, bd=0)
        self.listbox_example.place(x=self.calc.get_width(self.calc.body_center(90)), y=self.calc.get_height(self.calc.body_center(90)), width=200, height=200)
        self.components.append(self.listbox_example)
        self.components.append(self.button_example)
        self.components.append(self.label_example)
        self.set_theme()

    def set_theme(self):
        # toggle dark to white mode or white to dark mode
        if self.isDarkMode:
            self["bg"] = self.WHITE
            for widgets in self.components:
                widgets.config(bg=self.WHITE, fg=self.BLACK)
                if widgets == self.components[1]:
                    widgets.config(bg=self.WHITE, fg=self.BLACK, text=self.DARKMODE_TXT)
            self.isDarkMode = False
        else:
            self["bg"] = self.DARKMODE_COLOR
            for widgets in self.components:
                widgets.config(bg=self.DARKMODE_COLOR, fg=self.WHITE)
                if widgets == self.components[1]:
                    widgets.config(bg=self.DARKMODE_COLOR, fg=self.WHITE, text=self.WHITEMODE_TXT)
            self.isDarkMode = True


app = App(900, 600)
app.mainloop()
