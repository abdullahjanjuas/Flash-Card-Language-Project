#Importing libraries and modules
from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

#Reading csv and making dataframe using pandas
try:
    data = pandas.read_csv("Flash Project/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("Flash Project/data/french_words.csv")
    to_learn = original_data.to_dict(orient = "records")
else:
    to_learn = data.to_dict(orient = "records")
    
    
#Switches to next card
def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title,text = "French",fill = "black")
    canvas.itemconfig(card_word,text = current_card["French"],fill = "black")
    canvas.itemconfig(card_background, image = card_front)
    flip_timer = window.after(3000,flip_card) #Flips card after 3 sec

#Flips the card for english meaning    
def flip_card():  
    canvas.itemconfig(card_title,text = "English", fill = "white")
    canvas.itemconfig(card_word,text = current_card["English"],fill = "white")
    canvas.itemconfig(card_background, image = card_back)

#If user knows the word the we remove it from csv so user doesn't have to counter it again
def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("Flash Project/data/words_to_learn.csv",index = False)
    next_card()


#-----------------------------------UI------------------------------------------------#    
window = Tk()
window.title("Flashy")
window.config(padx = 58, pady = 58, bg = BACKGROUND_COLOR )


flip_timer = window.after(3000,flip_card) #Flips card after 3 sec

canvas = Canvas(width = 800 , height = 526)
card_front = PhotoImage(file = 'Flash Project/images/card_front.png')
card_back = PhotoImage(file = 'Flash Project/images/card_back.png')
card_background = canvas.create_image(400,263,image = card_front)
card_title = canvas.create_text(400,150,text = "Title", font = ("Ariel",40,"italic"))
card_word = canvas.create_text(400,263,text = "Word", font = ("Ariel",60,"bold"))
canvas.config(bg = BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row = 0, column = 0, columnspan = 2)

check_image = PhotoImage(file = 'Flash Project/images/right.png')
check_button = Button(image = check_image, highlightthickness = 0, command = is_known)
check_button.grid(row = 1, column = 0)

cross_image = PhotoImage(file = 'Flash Project/images/wrong.png')
cross_button = Button(image = cross_image, highlightthickness = 0,command = next_card)
cross_button.grid(row = 1, column = 1)

#Calls the function to display first french card after creating UI
next_card()





window.mainloop()