import random
import tkinter.messagebox
from tkinter import *

# Create an instance of Tkinter
root = Tk()

# Set the window title
root.title("Simple FPS Trainer V1")

# Set the window dimensions
root.geometry("600x350")

# Disable resizing of the window
root.resizable(False, False)

# The value of the countdown label
timeRemainingVar = StringVar(root, "Time remaining: 20")

# The value of the points label
pointsVar = StringVar(root, "0 points")

# Frame containing stats such:
#  - remaining time
#  - current points
statsFrame = Frame(
    root,
)

# Pack it at the top
statsFrame.pack(
    expand=False,
    fill='both',
    side='top'
)

# Add the label used for counting down
timeRemainingLabel = Label(
    statsFrame,
    textvariable=timeRemainingVar,
    bg="#323232",  # RGB: 50;  50;  50
    fg="#EAEEF5"  # RGB: 234; 238; 245
)

# Pack it inside statsFrame on the left
timeRemainingLabel.pack(
    ipadx=30,
    ipady=8,
    fill='x',
    expand=True,
    side='left'
)

# Label showing the current points
pointsLabel = Label(
    statsFrame,
    textvariable=pointsVar,
    bg="#323232",  # RGB: 50;  50;  50
    fg="#EAEEF5"  # RGB: 234; 238; 245
)

# Pack it inside statsFrame on the right
pointsLabel.pack(
    ipadx=30,
    ipady=8,
    fill='x',
    expand=True,
    side='right'
)

# Frame containing exercise widgets
gameFrame = Frame(
    root,
    bg="gray",
)

# Pack it on the bottom
gameFrame.pack(
    expand=True,
    fill='both',
    side='bottom'
)

# Create the label for the exercise
exerciseLabel = Label(
    gameFrame,
    text="Click to play",
    bg='#6E6E6E'  # RGB: 110; 110; 100
)

exerciseLabel.pack()

timeVar = StringVar(gameFrame, "20")

timeEntry = Entry(
    gameFrame,
    bg='#6E6E6E',
    textvariable=timeVar
)

timeEntry.pack()


def StartGame(event):
    global currentTime

    if timeVar.get().isnumeric():
        currentTime = int(timeVar.get())

    timeEntry.destroy()

    root.after(1000, DecreaseTimeRemaining)

    ExerciseComplete(0)


def Reset():
    global currentTime, currentPoints, timeEntry

    timeEntry = Entry(
        gameFrame,
        bg='#6E6E6E',
        textvariable=timeVar
    )

    timeEntry.pack()

    exerciseLabel.bind("<Button-1>", lambda event: ExerciseComplete(0))
    exerciseLabel.configure(text="Click to play")

    exerciseLabel.pack()

    currentTime = 20
    currentPoints = 0

    pointsVar.set(str(currentPoints) + " points")
    timeRemainingVar.set("Time remaining: " + str(currentTime))


def AskRetry() -> bool:
    return tkinter.messagebox.askyesno("Congratulations", f"You have {pointsVar.get()}\nDo you want to retry?")


currentPoints = 0


def AddPoints(new_points: int):
    global currentPoints

    currentPoints += new_points

    pointsVar.set(str(currentPoints) + " points")


currentTime = 20


def DecreaseTimeRemaining():
    global currentTime

    currentTime -= 1
    timeRemainingVar.set("Time remaining: " + str(currentTime))

    if currentTime == 0:
        for exer in exercises:
            exerciseLabel.unbind(exer[1])
            root.unbind(exer[1])

        exerciseLabel.bind("<Button-1>", StartGame)

        # Reset all the binds
        for exer in exercises:
            exerciseLabel.unbind(exer[1])
            root.unbind(exer[1])

        if AskRetry():
            Reset()
        else:
            root.destroy()
    else:
        root.after(1000, DecreaseTimeRemaining)


exercises = [
    ("Single Click", "<Button-1>", True),
    ("Double Click", "<Double-Button-1>", True),
    ("Triple Click", "<Triple-Button-1>", True),
    ("Press W", "w", False),
    ("Press A", "a", False),
    ("Press S", "s", False),
    ("Press D", "d", False),
    ("Press SPACE", "<space>", False)
]


def ExerciseComplete(points_to_add):
    randomExercise = random.choice(exercises)

    exerciseLabel.configure(text=randomExercise[0])

    # Place the exercise randomly on the screen
    exerciseLabel.place(
        anchor='center',
        width=80,
        height=25,
        x=random.randint(
            25,
            575
        ),

        y=random.randint(
            13,
            300
        )
    )

    for exer in exercises:
        exerciseLabel.unbind(exer[1])
        root.unbind(exer[1])

    # Bind the EVENT_NAME to call EVENT_HANDLER
    if randomExercise[2]:
        exerciseLabel.bind(randomExercise[1], lambda event: ExerciseComplete(2))
    else:
        root.bind(randomExercise[1], lambda event: ExerciseComplete(1))

    AddPoints(points_to_add)


exerciseLabel.bind("<Button-1>", StartGame)

root.mainloop()