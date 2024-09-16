from tkinter import Tk, Entry, Button, StringVar
import random

class Guesser:
    def __init__(self, master):
        master.title('Random Number Guesser')
        master.geometry('357x420+0+0')
        master.config(bg='gray')
        master.resizable(False, False)

        self.equation = StringVar()
        self.entry_value = ''
        Entry(width=17, bg='#fff', font=('Arial Bold', 28), textvariable=self.equation).place(x=0, y=0)

        while True:
            top_of_range = input("Type a number:  ")

            if top_of_range.isdigit():
                top_of_range = int(top_of_range)

                if top_of_range <= 0:
                    print("Please type a number larger than zero next time")
                    quit()
                else:
                    random_number = random.randint(1, top_of_range)  # Generate a random number between 1 and the given number
                    self.entry_value = str(random_number)
                    self.equation.set(self.entry_value)
                    break  # Exit the first while loop
            else:
                print("Please type a number next time")
                quit()

        Button(width=11, height=4, text='C', relief='flat', command=self.clear).place(x=0, y=350)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)


root = Tk()
guesser = Guesser(root)
root.mainloop()
