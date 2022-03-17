from tkinter import messagebox
from datetime import date
import tkinter as tk


def calculate():

    d0 = date(int(yearVar.get()), int(monthVar.get()), int(dayVar.get()))
    d1 = date.today()

    d2 = d0 - d1

    if d0 > d1:
        messagebox.askokcancel("Result", f"That is {d2.days} day(s) in the future")

    if d0 == d1:
        messagebox.askokcancel("Result", f"That is today!")

    if d0 < d1:
        messagebox.askokcancel("Result", f"That is {abs(d2.days)} day(s) in the past")


root = tk.Tk()

dayVar = tk.StringVar()
monthVar = tk.StringVar()
yearVar = tk.StringVar()


tk.Label(
    root,
    text="Date:"
).grid(row=1, column=1)

tk.Label(
    root,
    text="Day"
).grid(row=2, column=1)

tk.Spinbox(
    root,
    from_=1,
    to=31,
    textvariable=dayVar
).grid(row=2, column=2)

tk.Label(
    root,
    text="Month"
).grid(row=3, column=1)

tk.Spinbox(
    root,
    from_=1,
    to=12,
    textvariable=monthVar
).grid(row=3, column=2)

tk.Label(
    root,
    text="Year"
).grid(row=4, column=1)

tk.Spinbox(
    root,
    from_=1,
    to=9999,
    textvariable=yearVar
).grid(row=4, column=2)

tk.Button(
    root,
    text="Calculate",
    command=calculate
).grid(row=5, column=2)

root.mainloop()
