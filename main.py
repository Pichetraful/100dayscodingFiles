from tkinter import *

def button_clicked():
    print("I got clicked")
    new_text = round(float(input.get()) * 1.609, 2)
    my_label2.config(text=new_text)

window = Tk()
window.title("Miles to KM convertor")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# labels
my_label = Label(text="Is equal to", font=("Arial", 24, "bold"))
# my_label["text"] = "New Text"
#my_label.config(text="New Text")
# my_label.pack()
my_label.grid(column=0, row=1)

my_label2 = Label(text="0", font=("Arial", 24, "bold"))
my_label2.grid(column=1, row=1)

my_label3 = Label(text="Km", font=("Arial", 24, "bold"))
my_label3.grid(column=2, row=1)

my_label4 = Label(text="Miles", font=("Arial", 24, "bold"))
my_label4.grid(column=2, row=0)

# Button
button = Button(text="Click me", command=button_clicked)
# button.pack()
button.grid(column=1, row=2)

# Entry
input = Entry(width=10)
print(input.get())
# input.pack()
input.grid(column=1, row=0)



window.mainloop()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
