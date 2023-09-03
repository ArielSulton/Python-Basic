#1 -----===[ BASIC CODE ]===-----
"""
first = "Ariel"
last = "Sulton"
age = 18

print("hello "+first+" "+last.lower())
print("you are "+str(age)+" years old")
print("enjoy a nice day!")
"""

#2 -----===[ LIST, SET, TUPLE ]===-----
"""
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
"""
# List  = [] ordered and changeable. Duplicates OK
# Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER

#3 -----===[ WHILE LOOPS ]===-----
"""
name = ""

while len(name) == 0:
    name = input("your name : ")
    
print("hello "+name)
"""

#4 -----===[ FOR LOOPS ]===-----
"""
fruits = ["apple", "banana", "cherry"]
for i in fruits:
    if i == "banana":
        continue
        #break
    print(i)
"""

#5 -----===[ IF STATEMENT ]===-----
"""
age = int(input("Input your real age: "))

if age <= 17:
    print("you are under age!")

elif age > 17 and age < 40:
    print("you are ready to war")
    
else:
    print("you need to enjoy your life!")
"""

#6 -----===[ FUNCTION STATEMENT ]===-----
"""
def invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")

invoice("BroCode", 42.50, "01/02")
invoice("JoeSchmo", 100.99, "02/03")
"""

#7 -----===[ RETURN STATEMENT ]===-----
"""
def multiply(x,y):
    z=x*y
    return z

print(multiply(2,5))
"""

#8 -----===[ *ARGS ]===-----
#note: allow to pass multiple non-key arguments
"""
def add(*num):
    total = 0
    for i in num:
        total += i
    return total

print(add(1, 2, 3, 4))
"""
"""
def display_name(*args):
    print(f"Hello", end=" ")
    for i in args:
        print(i, end=" ")

display_name("Dr.", "Spongebob", "Harold", "Squarepants", "III")
"""

#9 -----===[ **KWARGS ]===-----
#note: allow to pass multiple key arguments
"""
def print_address(**kwargs):
    for i in kwargs.values():
        print(i, end=" ")

print_address(street="123 Fake St.",
                pobox="P.O Box 777",
                city="Detroit",
                state="MI",
                zip="54321")
"""

#10 -----===[ *ARGS & **KWARGS ]===-----
"""
def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('city')}, {kwargs.get('state')} {kwargs.get('zip')}")

shipping_label("Dr.", "Spongebob", "Squarepants",
                street="123 Fake St.",
                pobox="PO box #1001",
                city="Detroit",
                state="MI",
                zip="54321")
"""

#11 -----===[ RANDOM NUMBER ]===-----
"""
import random

x = random.randint(1,6) #integer
y = random.random() #float
#print (x+y)

myList = ["rock", 'paper', 'scissor']
z = random.choice(myList)
#print (z)

cards = [1,2,3,4,5,6,7,8,9,'J','Q','K','As']
random.shuffle(cards)
#print(cards)
"""

#12 -----===[ EXCEPTION HANDLING ]===-----
#note: exception is events detected during execution that interrupt the flow of a program
"""
try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator

except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero! idiot!")
except ValueError as e:
    print(e)
    print("Enter only numbers plz")
except Exception as e:
    print(e)
    print("something went wrong :(")
else:
    print(result)
finally:
    print("This will always execute")
    
"""

#13 -----===[ INHERITANCE ]===-----
"""
class Animal:

    alive = True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")

class Rabbit(Animal):

    def run(self):
        print("This rabbit is running")

class Fish(Animal):

    def swim(self):
        print("This fish is swimming")

class Hawk(Animal):

    def fly(self):
        print("This hawk is flying")


rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)
fish.eat()
hawk.sleep()

rabbit.run()
fish.swim()
hawk.fly()
"""

#14 -----===[ LAMBDA ]===-----
# lambda function = function written in 1 line using lambda keyword
#                   accepts any number of arguments, but only has one expression.
#                   (think of it as a shortcut)
#                   (useful if needed for a short period of time, throw-away)
#
# lambda parameters:expression
"""
double = lambda x: x * 2
print(double(1))

multiply = lambda x, y: x * y
print(multiply(1,2))

add = lambda x, y, z: x + y + z
print(add(1,2,3))

full_name = lambda first_name, last_name: first_name+" "+last_name
print(full_name("Bro","Code"))
"""

#15 -----===[ WINDOWS GUI ]===-----
"""
from tkinter import *
from PIL import Image, ImageTk

window = Tk() #initiate an instance of a window
window.geometry("420x420")
window.title("<try to be extrovert person/>")

icon = ImageTk.PhotoImage(file="logo.png")
window.iconphoto(True,icon)
window.config(background="#303030")

window.mainloop() #place window on computer screen, listen for events
"""

#16 -----===[ CALCULATOR APP ]===-----
"""
from tkinter import *

def button_press(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)

def equals():
    global equation_text

    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total

    except SyntaxError:
        equation_label.set("syntax error")
        equation_text = ""

    except ZeroDivisionError:
        equation_label.set("arithmetic error")
        equation_text = ""

def clear():
    global equation_text
    equation_label.set("")
    equation_text = ""


window = Tk()
window.title("Calculator program")
window.geometry("500x500")

equation_text = ""

equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=('consolas',20), bg="white", width=24, height=2)
label.pack()

frame = Frame(window)
frame.pack()

button1 = Button(frame, text=1, height=4, width=9, font=35,
                command=lambda: button_press(1))
button1.grid(row=0, column=0)

button2 = Button(frame, text=2, height=4, width=9, font=35,
                command=lambda: button_press(2))
button2.grid(row=0, column=1)

button3 = Button(frame, text=3, height=4, width=9, font=35,
                command=lambda: button_press(3))
button3.grid(row=0, column=2)

button4 = Button(frame, text=4, height=4, width=9, font=35,
                command=lambda: button_press(4))
button4.grid(row=1, column=0)

button5 = Button(frame, text=5, height=4, width=9, font=35,
                command=lambda: button_press(5))
button5.grid(row=1, column=1)

button6 = Button(frame, text=6, height=4, width=9, font=35,
                command=lambda: button_press(6))
button6.grid(row=1, column=2)

button7 = Button(frame, text=7, height=4, width=9, font=35,
                command=lambda: button_press(7))
button7.grid(row=2, column=0)

button8 = Button(frame, text=8, height=4, width=9, font=35,
                command=lambda: button_press(8))
button8.grid(row=2, column=1)

button9 = Button(frame, text=9, height=4, width=9, font=35,
                command=lambda: button_press(9))
button9.grid(row=2, column=2)

button0 = Button(frame, text=0, height=4, width=9, font=35,
                command=lambda: button_press(0))
button0.grid(row=3, column=0)

plus = Button(frame, text='+', height=4, width=9, font=35,
                command=lambda: button_press('+'))
plus.grid(row=0, column=3)

minus = Button(frame, text='-', height=4, width=9, font=35,
                command=lambda: button_press('-'))
minus.grid(row=1, column=3)

multiply = Button(frame, text='*', height=4, width=9, font=35,
                command=lambda: button_press('*'))
multiply.grid(row=2, column=3)

divide = Button(frame, text='/', height=4, width=9, font=35,
                command=lambda: button_press('/'))
divide.grid(row=3, column=3)

equal = Button(frame, text='=', height=4, width=9, font=35,
                command=equals)
equal.grid(row=3, column=2)

decimal = Button(frame, text='.', height=4, width=9, font=35,
                command=lambda: button_press('.'))
decimal.grid(row=3, column=1)

clear = Button(window, text='clear', height=4, width=12, font=35,
                command=clear)
clear.pack()

window.mainloop()
"""
#17 -----===[ .py to .exe ]===-----
"""
# (Windows Defender may prevent you from running)
# (make sure pip and pyinstaller are installed/updated)
#
# 1. cd to directory that contains your .py file
# 2. pyinstaller ...
#   -F          (all in 1 file)
#   -w          (removes terminal window)
#   -i icon.ico (adds custom icon to .exe)
#   clock.py    (name of your main python file)
#
# 3. exe is located in the dist folder
"""

#18 -----===[ null ]===-----

def null():
    return null