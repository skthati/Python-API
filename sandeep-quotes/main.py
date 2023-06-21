from tkinter import *
import random


def new_quote():
    with open("sandeep-quotes/my_quotes.txt") as my_quotes:
        data = my_quotes.readlines()
        data = [i[:-1] for i in data]
    
    this_quote = random.choice(data)

    canvas.itemconfig(n_quote, text=this_quote)



window = Tk()
window.title("Daddy Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="sandeep-quotes/background.png")
canvas.create_image(150, 207, image=background_img)
n_quote = canvas.create_text(150, 207, text="Daddy Quotes are here..", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

my_img = PhotoImage(file="sandeep-quotes/sandeep.png")
my_button = Button(image=my_img, highlightthickness=0, command=new_quote)
my_button.grid(row=1, column=0)

window.mainloop()


