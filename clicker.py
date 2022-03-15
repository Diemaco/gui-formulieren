import random
import tkinter as tk


def randomColor():
    return random.choice(["white", "black", "red", "green", "blue", "cyan", "yellow", "magenta"])


i = 0
lastClicked = ''

def up():
    global i, lastClicked
    i += 1

    checkbox.configure(state='normal')

    updateBg()
    amountStr.set(i)
    lastClicked = 'up'


def down():
    global i, lastClicked
    i -= 1

    checkbox.configure(state='normal')

    updateBg()
    amountStr.set(i)
    lastClicked = 'down'


def updateBg():
    if i == 0:
        root.configure(bg='gray')
    elif i > 0:
        root.configure(bg='green')
    elif i < 0:
        root.configure(bg='red')


def triple(e):
    global i, lastClicked

    lastClicked = 'triple'

    if lastClicked == 'up':
        i *= 3
    else:
        i //= 3

    amountStr.set(i)


def click():

    if isClicked.get():
        match lastClicked:
            case '':
                pass
            case 'up':
                up()
            case 'down':
                down()
            case 'triple':
                triple(None)

    root.after(5000, click)


root = tk.Tk()
root.title('Clicker')
root.configure(bg='gray')

root.bind('+', lambda e: up())
root.bind('-', lambda e: down())
root.bind('<Up>', lambda e: up())
root.bind('<Down>', lambda e: down())
root.bind('<space>', triple)

isClicked = tk.IntVar(value=0)

checkbox = tk.Checkbutton(
    root,
    state='disabled',
    variable=isClicked
)

checkbox.pack()

amountStr = tk.IntVar(value=0)

button = tk.Button(text='Up', bg=randomColor(), fg=randomColor())
button.pack(pady=20, padx=20)
button.configure(command=up)

text = tk.Label(root, bg=randomColor(), fg=randomColor())
text.configure(textvariable=amountStr)

text.bind('<Enter>', lambda e: root.configure(bg='yellow'))
text.bind('<Leave>', lambda e: updateBg())
text.bind('<Double-Button-1>', triple)

text.pack()

button = tk.Button(text='Down', bg=randomColor(), fg=randomColor())
button.pack(pady=20, padx=20)
button.configure(command=down)

root.after(5000, click)
root.mainloop()