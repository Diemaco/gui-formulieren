import tkinter as tk

root = tk.Tk()
root.geometry('500x500')

canvas = tk.Canvas(root)
canvas.pack(expand=True, fill='both')

length = 50
switch = True
for y in range(10):
    for x in range(10):
        canvas.create_rectangle(x * length, y * length, 500, 500, outline='', fill='red' if switch else 'blue')

        switch = not switch

    switch = not switch

root.mainloop()
