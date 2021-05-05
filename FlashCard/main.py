from pandas import *
from tkinter import *
from random import *

WHITE = "#FFFFFF"
BACKGROUND_COLOR = "#B1DDC6"

current_card = {}
learnwords = {}

#working with csv data
try:
    data = read_csv("data/words_to_learn.csv")
except:
    original_data = read_csv("data/french_words.csv")
    learnwords= original_data.to_dict(orient="records")
else:
    learnwords = data.to_dict(orient="records")


def on_click():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(learnwords)
    canvas.itemconfig(french_title, text="French", fill="black")
    canvas.itemconfig(fr_word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(french_title, text="English", fill="white")
    canvas.itemconfig(fr_word, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_background, image=card_back_img)


def is_known():
    learnwords.remove(current_card)
    data=DataFrame(learnwords)
    data.to_csv("data/words_to_learn.csv", index=False)
    on_click()

# UI
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg= BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

#Canvas
canvas = Canvas(width = 800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
#adding image to canvas
card_front_img = PhotoImage(file="images\card_front.png")
card_back_img = PhotoImage(file="images\card_back.png")
canvas_background = canvas.create_image(400, 263, image=card_front_img)

#adding word to canvas
french_title = canvas.create_text(400, 150,fill="black", font=("ariel", 40, "italic"))
fr_word = canvas.create_text(400, 263, fill="black", font=("ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

#wrongbutton
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, bd=0, command=on_click)
wrong_button.grid(row=1, column=0)

#rightbutton
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, bd=0, command=is_known)
right_button.grid(row=1, column=1)

on_click()
is_known()
window.mainloop()