from tkinter import *
from random import sample
from tkinter import messagebox
import datetime

# Creating a GUI that asks user to enter their age
date = datetime.datetime.now()
print(date)



window = Tk()
window.title("Age confirmation")
window.geometry("600x400")
window.config(bg="yellow")
li_rand = sample(range(1, 49), 6)
print(li_rand)
# Creating label and entry for name of player
name_label = Label(window, text="Please enter your name: ", font=("Comic Sans MS", 20), bg="yellow")
name_label.place(x=0, y=0)

name_entry = Entry(window, width=20)
name_entry.place(x=300, y=2)

# Creating the label and entry that allows users to enter if their age is correct
age_label = Label(window, text="Please enter your age: ", font=("Comic Sans Ms", 20), bg="yellow")
age_label.place(x=0, y=50)

age_entry = Entry(window, width=20)
age_entry.place(x=300, y=52)

# Declaring the name and age into Vars
name = name_entry.get()
age = age_entry.get()

# Creating a selection for player to choose lotto type
lotto_label = Label(window, text="Pick your poison: ", font=("Comic Sans MS", 20), bg="yellow")
lotto_label.place(x=0, y=100)
lotto_list = StringVar()
lotto_type = Listbox(window, width=20, height=5)
lotto_list = ("Lotto", "Lotto Plus", "Powerball")
for x in lotto_list:
    lotto_type.insert(END, str(x))
lotto_type.place(x=300, y=100)


# Defining the play button to enter the lottery if age is above 18 and to display a messagebox and raise an error is a string is entered
def play():
    from PIL import Image
    try:
        if int(age_entry.get()) < 18:
            messagebox.showinfo("OOPS", "No under 18s " + name_entry.get() + " , come back in a few years")
    except ValueError:
        messagebox.showinfo("OOPS", "Please enter a number " + name_entry.get())
        raise ValueError

    # Creating the lottery GUI for them to play
    else:
        if int(age_entry.get()) >= 18:
            window.withdraw()
            root = Tk()
            root.title("Welcome to Ithuba National Lottery of South Africa " + name_entry.get())
            root.geometry("700x500")
            root.config(bg="yellow")
            # Creating the label for the game
            open_label = Label(root, text="You feeling lucky " + name_entry.get() + "?", font=("Comic Sans MS", 20),
                               bg="yellow")
            open_label.place(x=200, y=0)


            # Creating entries for the user to enter their numbers
            num_label = Label(root, text="Enter your numbers", font=("Comic Sans MS", 20), bg="yellow")
            num_label.place(x=200, y=40)
            num1 = Entry(root, width=5)
            num1.place(x=120, y=80)
            num2 = Entry(root, width=5)
            num2.place(x=180, y=80)
            num3 = Entry(root, width=5)
            num3.place(x=240, y=80)
            num4 = Entry(root, width=5)
            num4.place(x=300, y=80)
            num5 = Entry(root, width=5)
            num5.place(x=360, y=80)
            num6 = Entry(root, width=5)
            num6.place(x=420, y=80)
            results = Label(root, text="Results:", bg="yellow", font=("Comic Sans MS", 20))
            results.place(x=200, y=250)

            # Defining the draw when user enters a number so it generates the new numbers and displays the results
            def draw():
                try:
                    user_numbers = [int(num1.get()), int(num2.get()), int(num3.get()), int(num4.get()), int(num5.get()),
                                    int(num6.get())]
                    print(user_numbers)

                    s = set(user_numbers).intersection(li_rand)
                    print(len(s))

                    if len(s) == 0:
                        results.config(text="your numbers were: " + str(user_numbers) + "\n" +
                                            "the winning numbers are: " +
                                            str(li_rand) + "\n" + "!!!!You earned nothing!!!!"+ "\n" + str(date))
                    if len(s) == 1:
                        results.config(text="your numbers were: " + str(user_numbers) + "\n" +
                                            "the winning numbers are: " +
                                            str(li_rand) + "\n" + "!!!!You earned nothing!!!!" + "\n" + str(date))

                    if len(s) == 2:
                        results.config(text="your numbers were: " + str(user_numbers) + "\n" +
                                            "the winning numbers are: " +
                                            str(li_rand) + "\n" + "you won R 20.00!!!!" + "\n" + str(date))

                    if len(s) == 3:
                        results.config(text="your numbers were: " + str(user_numbers) + "\n" +
                                            "the winning numbers are: " +
                                            str(li_rand) + "\n" + "you won R 100.50!!!!" + "\n" + str(date))

                    if len(s) == 4:
                        results.config(
                            text="your numbers were: " + str(user_numbers) + "\n" + "the winning numbers are: " +
                                 str(li_rand) + "\n" + "you won R 2384.00!!!!" + "\n" + str(date))

                    if len(s) == 5:
                        results.config(
                            text="your numbers were: " + str(user_numbers) + "\n" +
                                 "the winning numbers are: " +
                                 str(li_rand) + "\n" + "R 8584.00!!!!" + "\n" + str(date))

                    if len(s) == 6:
                        results.config(
                            text="your numbers were: " + str(user_numbers) + "\n" + "the winning numbers are: " +
                                 str(li_rand) + "\n" + "You won the jackpot: R 10 000 000.00" + "\n" + str(date))
                # Creating an error when the user enters a string
                except ValueError:
                    messagebox.showinfo("OOPS!", "Please enter a number")

                # Copying users numbers and winning numbers over to a text file

                f = open("result.txt", "w+")
                f.close()
                f = open("result.txt", "a")
                f.write(results.cget("text"))

            draw_button = Button(root, text="DRAW", command=draw)

            draw_button.place(x=0, y=180)

            # Defining and creating the try again button so user can play another round
            def try_again():
                num1.delete(0, 'end')
                num2.delete(0, 'end')
                num3.delete(0, 'end')
                num4.delete(0, 'end')
                num5.delete(0, 'end')
                num6.delete(0, 'end')

            again_button = Button(root, text="TRY AGAIN", command=try_again)
            again_button.place(x=600, y=180)


# Defining and Creating the clear button
def clear():
    name_entry.delete(0, 'end')
    age_entry.delete(0, 'end')


clear_button = Button(window, text="CLEAR", command=clear, width=20)
clear_button.place(x=300, y=300)


# Play button created
play_button = Button(window, text="PLAY", command=play, width=20)
play_button.place(x=40, y=300)


window.mainloop()
