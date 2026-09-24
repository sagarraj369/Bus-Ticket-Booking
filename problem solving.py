
import tkinter as tk
import math


# =========================================================
# WINDOW
# =========================================================

root = tk.Tk()
root.title("Calculator")
root.geometry("380x600")
root.resizable(False, False)
root.configure(bg="#151515")


# =========================================================
# COLORS
# =========================================================

BG = "#151515"
DISPLAY_BG = "#202020"
NUMBER_BG = "#2A2A2A"
NUMBER_HOVER = "#353535"
OPERATOR_BG = "#FF9500"
OPERATOR_HOVER = "#FFAA33"
SPECIAL_BG = "#3A3A3A"
SPECIAL_HOVER = "#4A4A4A"
TEXT = "#FFFFFF"
SECONDARY_TEXT = "#AAAAAA"


# =========================================================
# CALCULATOR VARIABLES
# =========================================================

expression = ""
display_value = "0"


# =========================================================
# DISPLAY
# =========================================================

display_frame = tk.Frame(
    root,
    bg=DISPLAY_BG,
    height=150
)

display_frame.pack(
    fill="x",
    padx=15,
    pady=(15, 10)
)

display_frame.pack_propagate(False)


# Small text showing expression
history_label = tk.Label(
    display_frame,
    text="",
    font=("Segoe UI", 13),
    bg=DISPLAY_BG,
    fg=SECONDARY_TEXT,
    anchor="e"
)

history_label.pack(
    fill="x",
    padx=18,
    pady=(15, 0)
)


# Main display
display_label = tk.Label(
    display_frame,
    text="0",
    font=("Segoe UI", 38, "bold"),
    bg=DISPLAY_BG,
    fg=TEXT,
    anchor="e"
)

display_label.pack(
    fill="both",
    expand=True,
    padx=18,
    pady=(0, 10)
)


# =========================================================
# FUNCTIONS
# =========================================================

def update_display():
    """Update calculator display."""

    if expression:
        display_label.config(text=expression)
    else:
        display_label.config(text="0")


def press(value):
    """Add a number or operator."""

    global expression

    # If calculator currently shows an error
    if expression == "Error":
        expression = ""

    # Prevent multiple decimal points in one number
    if value == ".":

        current_number = ""

        for char in reversed(expression):
            if char in "+-*/%":
                break
            current_number = char + current_number

        if "." in current_number:
            return

    # Prevent two operators together
    if value in "+-*/%":

        if expression == "":
            if value == "-":
                expression = "-"
                update_display()
            return

        if expression[-1] in "+-*/%":
            expression = expression[:-1]

    expression += value

    update_display()


def clear():
    """Clear calculator."""

    global expression

    expression = ""

    history_label.config(text="")

    update_display()


def backspace():
    """Delete last character."""

    global expression

    if expression == "Error":
        expression = ""
    else:
        expression = expression[:-1]

    update_display()


def calculate():
    """Calculate expression."""

    global expression

    if not expression:
        return

    try:
        # Replace percentage with division by 100
        calculation = expression.replace("%", "/100")

        result = eval(
            calculation,
            {"__builtins__": None},
            {}
        )

        # Remove unnecessary .0
        if isinstance(result, float) and result.is_integer():
            result = int(result)

        history_label.config(
            text=expression + " ="
        )

        expression = str(result)

        update_display()

    except:
        expression = "Error"
        display_label.config(text="Error")


def square():
    """Square current number."""

    global expression

    try:
        result = eval(
            expression,
            {"__builtins__": None},
            {}
        )

        result = result ** 2

        if isinstance(result, float) and result.is_integer():
            result = int(result)

        history_label.config(
            text=expression + "²"
        )

        expression = str(result)

        update_display()

    except:
        expression = "Error"
        update_display()


def square_root():
    """Calculate square root."""

    global expression

    try:
        result = eval(
            expression,
            {"__builtins__": None},
            {}
        )

        result = math.sqrt(result)

        if result.is_integer():
            result = int(result)

        history_label.config(
            text="√" + expression
        )

        expression = str(result)

        update_display()

    except:
        expression = "Error"
        update_display()


def toggle_sign():
    """Change positive number to negative."""

    global expression

    try:
        result = eval(
            expression,
            {"__builtins__": None},
            {}
        )

        result = -result

        if isinstance(result, float) and result.is_integer():
            result = int(result)

        expression = str(result)

        update_display()

    except:
        pass


# =========================================================
# BUTTON FUNCTIONS
# =========================================================

def button_click(value):

    if value == "C":
        clear()

    elif value == "⌫":
        backspace()

    elif value == "=":
        calculate()

    elif value == "x²":
        square()

    elif value == "√":
        square_root()

    elif value == "±":
        toggle_sign()

    else:
        press(value)


# =========================================================
# BUTTON HOVER EFFECT
# =========================================================

def add_hover(button, normal_color, hover_color):

    def on_enter(event):
        button.config(bg=hover_color)

    def on_leave(event):
        button.config(bg=normal_color)

    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)


# =========================================================
# BUTTON AREA
# =========================================================

button_frame = tk.Frame(
    root,
    bg=BG
)

button_frame.pack(
    padx=15,
    pady=5,
    fill="both",
    expand=True
)


# =========================================================
# BUTTON CREATION
# =========================================================

def create_button(
    text,
    row,
    column,
    color=NUMBER_BG,
    hover_color=NUMBER_HOVER,
    columnspan=1
):

    button = tk.Button(
        button_frame,
        text=text,
        font=("Segoe UI", 17, "bold"),
        bg=color,
        fg=TEXT,
        activebackground=hover_color,
        activeforeground=TEXT,
        bd=0,
        relief="flat",
        cursor="hand2",
        command=lambda: button_click(text)
    )

    button.grid(
        row=row,
        column=column,
        columnspan=columnspan,
        padx=5,
        pady=5,
        sticky="nsew"
    )

    add_hover(
        button,
        color,
        hover_color
    )

    return button


# =========================================================
# GRID CONFIGURATION
# =========================================================

for i in range(5):
    button_frame.rowconfigure(
        i,
        weight=1
    )

for i in range(4):
    button_frame.columnconfigure(
        i,
        weight=1
    )


# =========================================================
# TOP ROW
# =========================================================

create_button(
    "C",
    0,
    0,
    SPECIAL_BG,
    SPECIAL_HOVER
)

create_button(
    "⌫",
    0,
    1,
    SPECIAL_BG,
    SPECIAL_HOVER
)

create_button(
    "√",
    0,
    2,
    SPECIAL_BG,
    SPECIAL_HOVER
)

create_button(
    "/",
    0,
    3,
    OPERATOR_BG,
    OPERATOR_HOVER
)


# =========================================================
# SECOND ROW
# =========================================================

create_button("7", 1, 0)
create_button("8", 1, 1)
create_button("9", 1, 2)

create_button(
    "*",
    1,
    3,
    OPERATOR_BG,
    OPERATOR_HOVER
)


# =========================================================
# THIRD ROW
# =========================================================

create_button("4", 2, 0)
create_button("5", 2, 1)
create_button("6", 2, 2)

create_button(
    "-",
    2,
    3,
    OPERATOR_BG,
    OPERATOR_HOVER
)


# =========================================================
# FOURTH ROW
# =========================================================

create_button("1", 3, 0)
create_button("2", 3, 1)
create_button("3", 3, 2)

create_button(
    "+",
    3,
    3,
    OPERATOR_BG,
    OPERATOR_HOVER
)


# =========================================================
# BOTTOM ROW
# =========================================================

create_button("±", 4, 0)
create_button("0", 4, 1)
create_button(".", 4, 2)

create_button(
    "=",
    4,
    3,
    OPERATOR_BG,
    OPERATOR_HOVER
)


# =========================================================
# KEYBOARD SUPPORT
# =========================================================

def keyboard_input(event):

    key = event.keysym
    char = event.char

    if char in "0123456789.+-*/%":
        press(char)

    elif key == "Return":
        calculate()

    elif key == "BackSpace":
        backspace()

    elif key == "Escape":
        clear()


root.bind("<Key>", keyboard_input)


# =========================================================
# START
# =========================================================

root.mainloop()


