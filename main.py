import tkinter as tk
from tkinter import *
from random import randint
from PIL import Image, ImageTk


global wins
wins = 0
global losses
losses = 0

global playerImage
playerImage = None
global computerImage
computerImage = None


def tick():
    global wins
    global losses
    # win.config(text="Wins: {}".format(wins))
    # loss.config(text="Losses: {}".format(losses))
    print(wins)


def rock():  # 0
    global losses
    global wins
    global playerImage

    playerImage = rockImage

    random = computer_throw()

    if random == 0:  # Rock
        tieEvent()
    elif random == 1:  # Paper
        loseEvent()
    elif random == 2:  # Scissors
        winEvent()
    labelUpdate()
    playerCanvas.itemconfig(playerOld, image=playerImage)
    computerCanvas.itemconfig(computerOld, image=computerImage)


def paper():  # 1
    global losses
    global wins
    global playerImage

    playerImage = paperImage

    random = computer_throw()

    if random == 0:  # Rock
        winEvent()
    elif random == 1:  # Paper
        tieEvent()
    elif random == 2:  # Scissors
        loseEvent()
    labelUpdate()
    playerCanvas.itemconfig(playerOld, image=playerImage)
    computerCanvas.itemconfig(computerOld, image=computerImage)

def scissors():  # 2
    global losses
    global wins
    global playerImage

    playerImage = scissorsImage

    random = computer_throw()

    if random == 0:  # Rock
        loseEvent()
    elif random == 1:  # Paper
        winEvent()
    elif random == 2:  # Scissors
        tieEvent()
    labelUpdate()
    playerCanvas.itemconfig(playerOld, image=playerImage)
    computerCanvas.itemconfig(computerOld, image=computerImage)


def computer_throw():
    global computerImage

    random = randint(0, 2)

    if random == 0:
        computerImage = rockImage
    elif random == 1:
        computerImage = paperImage
    elif random == 2:
        computerImage = scissorsImage

    return random

# Updates win and loss labels after each match
def labelUpdate():
    winCount.set(wins)
    loseCount.set(losses)


# Executes whenever you win a match
def winEvent():
    global wins
    wins += 1
    print("Player wins!")
    matchResult.set("Player wins!")


# Executes whenever you lose a match
def loseEvent():
    global losses
    losses += 1
    print("Player loses.")
    matchResult.set("Player loses.")


# Executes whenever you tie a match
def tieEvent():
    print("Draw.")
    matchResult.set("Draw.")


root = Tk()

# Set up stringVars to store the number of wins and losses
winCount = tk.StringVar()
winCount.set(0)
loseCount = tk.StringVar()
loseCount.set(0)
matchResult = tk.StringVar()
matchResult.set("")

# # Set image variables and file paths
rockImage = Image.open("RockImage.jpg")
rockImage = rockImage.resize((200, 200), Image.ANTIALIAS)
rockImage = ImageTk.PhotoImage(rockImage)
paperImage = Image.open("PaperImage.jpg")
paperImage = paperImage.resize((200, 200), Image.ANTIALIAS)
paperImage = ImageTk.PhotoImage(paperImage)
scissorsImage = Image.open("ScissorsImage.jpg")
scissorsImage = scissorsImage.resize((200, 200), Image.ANTIALIAS)
scissorsImage = ImageTk.PhotoImage(scissorsImage)

# Set Window Size
root.geometry("1200x600")
root.resizable(0, 0)

# "Win" label (tracks total number of wins)
winText = Label(root, font=("times", 50, "bold"), text="Wins: ")
winText.grid(row=0, column=1)
win = Label(root, font=("times", 50, "bold"), textvariable=winCount)
win.grid(row=0, column=2)

# "Loss" label (tracks total number of losses)
lossText = Label(root, font=("times", 50, "bold"), text="Losses: ")
lossText.grid(row=1, column=1)
loss = Label(root, font=("times", 50, "bold"), textvariable=loseCount)
loss.grid(row=1, column=2)

# Labels display player and computer choices
playerChoice = Label(root, font=("times", 25, "bold"), text=" Player choice: ")
playerChoice.grid(row=2, column=2)
computerChoice = Label(root, font=("times", 25, "bold"), text="Computer choice:")
computerChoice.grid(row=2, column=4)

# Images to display player and computer choices
playerCanvas = Canvas(root, width=200, height=200)
playerCanvas.grid(row=3, column=2)
playerOld = playerCanvas.create_image(0, 0, anchor=NW, image=None)
computerCanvas = Canvas(root, width=200, height=200)
computerCanvas.grid(row=3, column=4)
computerOld = computerCanvas.create_image(0, 0, anchor=NW, image=None)

# Label to display match results
results = Label(root, font=("times", 25, "italic"), textvariable=matchResult)
results.grid(row=4, column=3)
# Rock Button
rock = Button(root, font=("times", 25), text="Rock", command=rock)
rock.grid(row=5, column=1, padx=0)  # padx creates space on the x axis

# Paper Button
paper = Button(root, font=("times", 25), text="Paper", command=paper)
paper.grid(row=5, column=3, padx=40)

# Scissors Button
scissors = Button(root, font=("times", 25), text="Scissors", command=scissors)
scissors.grid(row=5, column=5, pady=30, padx=65)  # pady creates space on the y axis


tick()
root.mainloop()
