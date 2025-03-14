from tkinter import *
from tkinter import messagebox
import base64

def process_text(action):
    """Handles both encryption and decryption based on the action parameter."""
    password = code.get()
    if password != "1234":
        messagebox.showerror("Error", "Invalid Secret Key!")
        return

    message = text1.get(1.0, END).strip()

    if not message:
        messagebox.showwarning("Warning", "Text field is empty!")
        return

    try:
        if action == "encrypt":
            processed_text = base64.b64encode(message.encode("ascii")).decode("ascii")
            bg_color, title = "#ed3833", "Encryption"
        else:  # Decryption
            processed_text = base64.b64decode(message.encode("ascii")).decode("ascii")
            bg_color, title = "#00bd56", "Decryption"

        # Create a new window for output
        result_screen = Toplevel(screen)
        result_screen.title(title)
        result_screen.geometry("400x200")
        result_screen.config(bg=bg_color)

        Label(result_screen, text=title.upper(), font="arial", fg="white", bg=bg_color).pack(pady=10)

        text_output = Text(result_screen, font="Robote 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text_output.pack(padx=10, pady=5, fill=BOTH, expand=True)
        text_output.insert(END, processed_text)
        text_output.config(state=DISABLED)  # Make text read-only

    except Exception as e:
        messagebox.showerror("Error", "Invalid input for decryption!")


def reset_fields():
    """Clears text input fields."""
    code.set("")
    text1.delete(1.0, END)


def main_screen():
    global screen, code, text1

    screen = Tk()
    screen.geometry("375x398")
    screen.title("Encryption and Decryption")

    # Icon handling
    try:
        image_icon = PhotoImage(file="encryption.png")
        screen.iconphoto(False, image_icon)
    except:
        print("Warning: encryption.png not found!")

    Label(screen, text="Enter text for encryption and decryption", fg="black", font=("calibri", 13)).pack(pady=5)

    text1 = Text(screen, font="Robote 20", bg="white", relief=GROOVE, wrap=WORD, bd=0, height=5)
    text1.pack(padx=10, pady=5, fill=BOTH, expand=False)

    Label(screen, text="Enter secret key for encryption and decryption", fg="black", font=("calibri", 13)).pack(pady=5)

    code = StringVar()
    Entry(screen, textvariable=code, width=19, bd=0, font=("arial", 25), show="*").pack(pady=5)

    # Buttons
    frame = Frame(screen)
    frame.pack(pady=10)

    Button(frame, text="ENCRYPT", width=12, bg="#ed3833", fg="white", bd=0,
           command=lambda: process_text("encrypt")).grid(row=0, column=0, padx=5)
    Button(frame, text="DECRYPT", width=12, bg="#00bd56", fg="white", bd=0,
           command=lambda: process_text("decrypt")).grid(row=0, column=1, padx=5)
    Button(screen, text="RESET", width=25, bg="#1089ff", fg="white", bd=0,
           command=reset_fields).pack(pady=5)

    screen.mainloop()


main_screen()
