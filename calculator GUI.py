import tkinter as tk
import math


def click(event):
    text = event.widget.cget("text")
    
    if text == "=":
        try:
            result = str(eval(screen.get()))
            screen_var.set(result)
        except Exception as e:
            screen_var.set("Error")
    elif text == "C":
        screen_var.set("")
    elif text == "√":
        try:
            value = float(screen.get())
            result = math.sqrt(value)
            screen_var.set(result)
        except:
            screen_var.set("Error")
    elif text == "%":
        try:
            value = float(screen.get())
            result = value / 100
            screen_var.set(result)
        except:
            screen_var.set("Error")
    else:
        screen_var.set(screen_var.get() + text)


root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")
root.resizable(False, False)

screen_var = tk.StringVar()
screen = tk.Entry(root, textvar=screen_var, font="Arial 20", justify="right", bd=8, relief="ridge")
screen.pack(fill="x", ipadx=8, pady=10, padx=10)


button_texts = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C", "√", "%"]
]

for row_values in button_texts:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for val in row_values:
        button = tk.Button(
            frame, text=val, font="Arial 16 bold",
            relief="ridge", bd=3, padx=10, pady=10, bg="#f0f0f0", activebackground="#d9d9d9"
        )
        button.pack(side="left", expand=True, fill="both")
        button.bind("<Button-1>", click)

root.mainloop()

