import tkinter as tk
def click():
    print("how are you!")

window = tk.Tk()
window.title("My Program")

button = tk.Button(window,
text="Click Me", command=click)
button.pack(pady=20)

window.mainloop()
