# Tkinter Calculator

This is a simple calculator application built using Python's Tkinter library. It provides a basic graphical user interface for performing arithmetic calculations with a visually appealing rainbow color scheme for the buttons.

## Features

* Standard arithmetic operations: addition (+), subtraction (-), multiplication (x), and division (/).
* Parentheses for order of operations.
* Clear button ('C') to reset the display.
* Equals button ('=') to calculate the result.
* Error handling to display "Error" for invalid expressions.
* Visually appealing rainbow color scheme for buttons.

## Prerequisites

* Python 3.x
* Tkinter (This is usually included with standard Python installations)

## How to Run

1.  **Clone the repository:**

    ```bash
    git clone <your_repository_url>
    ```

2.  **Navigate to the project directory:**

    ```bash
    cd <your_repository_directory>
    ```

3.  **Run the script:**

    ```bash
    python calculator.py
    ```

## Code Explanation

* `calculator.py`: This is the main Python file containing the calculator application's code. It uses the Tkinter library for the GUI.
* The code defines a `Calculator` class that handles the GUI creation, button events, and calculation logic.
* Tkinter's `Tk` class is used to create the main window.
* `Entry` widget is used for the display.
* `Button` widgets are used to create the calculator buttons.
* The `eval()` function is used to evaluate the mathematical expressions (with caution - see security note below).

## Code Structure
