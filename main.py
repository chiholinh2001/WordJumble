from tkinter import *
from random import choice
from random import shuffle
from tkinter import messagebox

linkIcon = "D:\Projects\WordJumble\icon.ico"

root = Tk()
root.title('Word Jumble')
root.geometry("600x400")
root.iconbitmap(linkIcon)

myLabel = Label(root, text="", font=("Helvetica", 50))
myLabel.pack(pady=20)

score = 0
timeleft = 60


def startGame(event):
    if timeleft == 60:
        countdown()
        shuffler()
        scorelabel.config(text="Score: 0")
    else:
        answer()


def countdown():
    global timeleft
    if timeleft == 0:
        messagebox.showinfo("Time Over", "Time is over and your score is " + str(score))
    if timeleft > 0:
        timeleft -= 1
        timelabel.config(text="Time Left: " + str(timeleft))
        timelabel.after(1000, countdown)


def shuffler():
    eAnswer.delete(0, END)
    # ansLabel.config(text="")
    ansLabel.after(400, lambda: ansLabel.config(text=''))

    global word
    Countries = ['Egypt', 'Sudan', 'Oman', 'Yemen', 'Syria', 'Algeria', 'Qatar', 'Lebanon', 'Tunisia', 'Libya',
                 'Kuwait', 'Jordan', 'Iraq', 'France', 'Germany', 'Spain', 'China', 'India', 'Canada', 'Brazil',
                 'Italy', 'Poland', 'Sweden', 'Norway', 'Greece', 'Netherlands', 'Japan', 'Iran', 'Portugal', 'Mexico',
                 'Cuba', 'Argentina', 'Colombia']

    word = choice(Countries)

    breakWord = list(word)
    shuffle(breakWord)

    global shuffled
    shuffled = ''
    for letter in breakWord:
        shuffled += letter

    myLabel.config(text=shuffled)


def answer():
    global score
    global timeleft

    if timeleft > 0:
        eAnswer.focus_set()
        if eAnswer.get().lower() == word.lower():
            score += 1
            ansLabel.config(text="Correct!")
        else:
            ansLabel.config(text="Incorrect")
        scorelabel.config(text="Score: " + str(score))

        shuffler()


scorelabel = Label(root, text="Enter to start", font=('Helvetica', 24))
scorelabel.pack()

timelabel = Label(root, text="Time left: " + str(timeleft), font=('Helvetica', 12))
timelabel.pack()

eAnswer = Entry(root, font=("Helvetica", 25))
eAnswer.pack(pady=20)

myFrame = Frame(root)
myFrame.pack(pady=20)

ansButton = Button(myFrame, text="Answer", command=answer)
ansButton.grid(row=0, column=1, padx=10)

ansLabel = Label(root, text="", font=("Helvetica", 20))
ansLabel.pack(pady=20)

root.bind('<Return>', startGame)
eAnswer.focus_set()

root.mainloop()
