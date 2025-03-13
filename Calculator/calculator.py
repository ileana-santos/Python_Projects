from tkinter import Tk, Entry, Button, StringVar
from typing import Callable, List, Tuple, Union

class Calculator:
    """
    A simple calculator application using Tkinter.
    """

    def __init__(self, master: Tk) -> None:
        """
        Initializes the Calculator application.

        Args:
            master (Tk): The root Tkinter window.
        """
        master.title("Calculator")
        master.geometry("357x420+0+0")
        master.configure(bg="white")
        master.resizable(False, False)

        self.equation: StringVar = StringVar()
        self.entry_value: str = ''

        Entry(master, width=17, bg='#fff', font=('Arial Bold', 28), textvariable=self.equation, justify='right').place(x=0, y=0)

        # Rainbow colors for buttons
        colors: List[str] = ["#FF0000", "#FF7F00", "#FFFF00", "#00FF00", "#0000FF", "#8B00FF"]

        # Button data (text, color index, x, y, command function)
        buttons: List[Tuple[Union[str, int], ...]] = [
            ('(', 0, 0, 50), (')', 0, 90, 50), ('%', 0, 180, 50), ('/', 0, 270, 50),
            ('7', 1, 0, 125), ('8', 1, 90, 125), ('9', 1, 180, 125), ('x', 1, 270, 125),
            ('4', 2, 0, 200), ('5', 2, 90, 200), ('6', 2, 180, 200), ('-', 2, 270, 200),
            ('1', 3, 0, 275), ('2', 3, 90, 275), ('3', 3, 180, 275), ('+', 3, 270, 275),
            ('0', 4, 90, 350), ('.', 4, 180, 350), ('=', 4, 270, 350, 'solve'),
            ('C', 5, 0, 350, 'clear')
        ]

        # Create buttons dynamically
        for btn in buttons:
            text: str = str(btn[0])  # Explicitly cast to str
            color_idx: int = btn[1]
            x: int = btn[2]
            y: int = btn[3]
            command: Callable[[], None]

            if len(btn) == 5:
                command = getattr(self, str(btn[4]))  # Ensure btn[4] is treated as a string
            else:
                command = lambda val=text: self.show(val)

            Button(master, width=11, height=4, text=text, relief='flat', bg=colors[color_idx], bd=3, command=command).place(x=x, y=y)

    def show(self, value: str) -> None:
        """
        Appends the given value to the entry field and updates the display.

        Args:
            value (str): The value to append.
        """
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self) -> None:
        """
        Clears the entry field and resets the display.
        """
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self) -> None:
        """
        Evaluates the expression in the entry field and displays the result.
        Displays "Error" if evaluation fails.
        """
        try:
            result: float = eval(self.entry_value)
            self.equation.set(result)
            self.entry_value = str(result)
        except Exception:
            self.equation.set("Error")
            self.entry_value = ''

root: Tk = Tk()
calculator: Calculator = Calculator(root)
root.mainloop()