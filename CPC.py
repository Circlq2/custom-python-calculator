# E G Wisnewski
# 15/09/2022

#*****************************************************
# Python Calculator with GUI (Graphic User interface)
#*****************************************************

from tkinter import * # import the tkinter library

def button_press(num):    # defining each button press
    global equation_text

    equation_text = equation_text + str(num)

    equation_label.set(equation_text)

def equals():     # this block checks for the button_press(equals)
    global equation_text

    try:    # try is used in try... except blocks. It defines a block of code test if it contains any errors.
            # You can define different blocks for different error types, and blocks to execute if nothing went wrong.
        total = str(eval(equation_text)) # parses the expression arguement is as a python expression.

        equation_label.set(total)

        equation_text = total

    except SyntaxError:    # Check for syntax error

        equation_label.set("syntax error")

        equation_text = ""

    except ZeroDivisionError:   # Check for division by zero

        equation_label.set("arithmetic error")

        equation_text = ""

def clear():        # clear the equation_label for the next calculation
    global equation_text

    equation_label.set("")

    equation_text = ""




# Designing the user interface

window = Tk()   # you can use window, root, ... or a descriptive varible of your own
window.title("Python Calculator")   # title in the window bar
window.geometry("350x425")   # size of the window dependent on your design
window.configure(bg="#cceaed")   # Window colour dependent on your design

equation_text = ""  # starting off with no text in label

equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=('console', 20), bg="#03ffaf", width=18, height=2)
# Set to stand out from the rest so they can see it easily
label.pack()   # widgets have to be "pack"ed into the window

frame = Frame(window)
frame.pack()    # the frame is a widget 

button1 = Button(frame, text=1, height=3, width=7, font=35, command=lambda: button_press(1))
button1.grid(row=0, column=0)

button2 = Button(frame, text=2, height=3, width=7, font=35, command=lambda: button_press(2))
button2.grid(row=0, column=1)

button3 = Button(frame, text=3, height=3, width=7, font=35, command=lambda: button_press(3))
button3.grid(row=0, column=2)

button4 = Button(frame, text=4, height=3, width=7, font=35, command=lambda: button_press(4))
button4.grid(row=1, column=0)

button5 = Button(frame, text=5, height=3, width=7, font=35, command=lambda: button_press(5))
button5.grid(row=1, column=1)

button6 = Button(frame, text=6, height=3, width=7, font=35, command=lambda: button_press(6))
button6.grid(row=1, column=2)

button7 = Button(frame, text=7, height=3, width=7, font=35, command=lambda: button_press(7))
button7.grid(row=2, column=0)

button8 = Button(frame, text=8, height=3, width=7, font=35, command=lambda: button_press(8))
button8.grid(row=2, column=1)

button9 = Button(frame, text=9, height=3, width=7, font=35, command=lambda: button_press(9))
button9.grid(row=2, column=2)

button0 = Button(frame, text=0, height=3, width=7, font=35, command=lambda: button_press(0))
button0.grid(row=3, column=1)

# create operation buttons
# All same colour to signal that they all are operations
plus = Button(frame, bg="#b961e8", text='+', height=3, width=7, font=35, command=lambda: button_press('+'))
plus.grid(row=0, column=3)

minus = Button(frame, bg="#b961e8", text='-', height=3, width=7, font=35, command=lambda: button_press('-'))
minus.grid(row=1, column=3)

multiply = Button(frame, bg="#b961e8", text='*', height=3, width=7, font=35, command=lambda: button_press('*'))
multiply.grid(row=2, column=3)

divide = Button(frame, bg="#b961e8", text='/', height=3, width=7, font=35, command=lambda: button_press('/'))
divide.grid(row=3, column=3)

# create equals button
# The colour is there to signal that it is an operation but not as important as the others
equal = Button(frame, bg="#e8eb46", text='=', height=3, width=7, font=35, command=equals)
equal.grid(row=3, column=2)

# create the decimal button
# The colour is there to signal that it is an operation but not as important as the others
decimal = Button(frame,bg="#e8eb46", text='.', height=3, width=7, font=35, command=lambda: button_press('.'))
decimal.grid(row=3, column=0)

# create clear button
# Pinkish colour to make the clear button stand out
clear = Button(window, bg="#ed9898", text='clear', height=3, width=10, font=35, command=clear)
clear.pack()


window.mainloop()

