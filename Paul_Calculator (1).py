
# coding: utf-8

# In[ ]:


#Justin Paul
#October 28th 2018
#SECZ82-1188 
#This program will create a calculator that will perform addition, subtraction, multiplication and division.
#import operator and import tkinter to open GUI.
import operator
from tkinter import *
#Define each number to appear within the screen of the calculator. This will insert the value into to the text display.
def zero():
    txtdisplay.insert(END, '0')
def one():
    txtdisplay.insert(END, '1')
def two():
    txtdisplay.insert(END, '2')
def three():
    txtdisplay.insert(END, '3')
def four():
    txtdisplay.insert(END, '4')
def five():
    txtdisplay.insert(END, '5')
def six():
    txtdisplay.insert(END, '6')
def seven():
    txtdisplay.insert(END, '7')
def eight():
    txtdisplay.insert(END, '8')
def nine():
    txtdisplay.insert(END, '9')
#Allows for each value to end with a decimal point. 
def decimal():
    if '.' not in txtdisplay.get():
        txtdisplay.insert(END, '.')
#Define the four basic operations by using their operators while using a global variable. This will perform the neccessary 
#calculations. 
def add():
    global n1, operation
    operation = operator.add
    n1 = float(txtdisplay.get()) #Use a float to return a real number when calculating.
    txtdisplay.delete(0, END)
    
def subtract():
    global n1,operation
    operation = operator.sub
    n1= float(txtdisplay.get())
    txtdisplay.delete(0,END)
def multiplication():
    global n1,operation
    operation= operator.mul
    n1= float(txtdisplay.get())
    txtdisplay.delete(0,END)
def division():
    global n1,operation
    operation= operator.truediv
    n1=float(txtdisplay.get())
    txtdisplay.delete(0,END)
    
#Define the equal operation while using an if statement. Your operation will be none as it will not be performing an operation.

def equal():
    global operation
    n2 = float(txtdisplay.get())
    txtdisplay.delete(0, END)

    if operation:
        txtdisplay.insert(0, str(operation(n1, n2)))
        operation = None
#define clear operation to erase all values after the clear button is hit.
def clear():
    global n1, operation
    n1 = 0.0
    operation = None
    txtdisplay.delete(0, END)
#the n1 represents the initial variable used when calculating. 
n1 = 0.0
operation = None
win = Tk()#what starts the GUI
win.title('Justin Calculator')#title of the calculator being programmed
#options represents the geometry options for the layout of calculator.
options = {'padx':6, 'pady':6, 'bd':5}
sticky = {'sticky': (N, S, E, W)}# sticky expands the widgets if the cell is larger. 
#the frame represents how the calculator will be laid out once it is in the GUI.
frame = Frame(win)
frame.pack()
#Text display that shows the values being calculated.
txtdisplay = Entry(frame, bd=30, insertwidth=1, font=30)
txtdisplay.grid(row=0, columnspan=4)
#Involves all buttons used on the calculator and geometrical alignments. Individual commands are listed.
#The most notable would be the exit button which will automatically exit the window. 
Button(frame, text='-', fg='black',command=subtract, **options).grid(row=1, column=3, **sticky)
Button(frame, text='*', fg='black',command=multiplication, **options).grid(row=1, column=2, **sticky)
Button(frame, text='/', fg='black',command=division, **options).grid(row=1, column=1, **sticky)

Button(frame, text='7', command=seven, fg='black', **options).grid(row=2, column=0, **sticky)
Button(frame, text='8', command=eight, fg='black', **options).grid(row=2, column=1, **sticky)
Button(frame, text='9', command=nine, fg='black', **options).grid(row=2, column=2, **sticky)

Button(frame, text='4', command=four, fg='red', **options).grid(row=3, column=0, **sticky)
Button(frame, text='5', command=five, fg='red', **options).grid(row=3, column=1, **sticky)
Button(frame, text='6', command=six, fg='red', **options).grid(row=3, column=2, **sticky)

Button(frame, text='1', command=one, fg='blue', **options).grid(row=4, column=0, **sticky)
Button(frame, text='2', command=two, fg='blue', **options).grid(row=4, column=1, **sticky)
Button(frame, text='3', command=three, fg='blue', **options).grid(row=4, column=2, **sticky)

Button(frame, text='0', command=zero, fg='black', **options).grid(row=5, column=1, **sticky)
Button(frame, text='.', command=decimal, fg='black', **options).grid(row=5, column=2, **sticky)
Button(frame, text='Exit', command=win.destroy, fg='black', **options).grid(row=5, column=0, **sticky)

Button(frame, text='+', command=add, fg='black', **options).grid(row=2, column=3, rowspan=2, **sticky)
Button(frame, text='=', command=equal, fg='black', **options).grid(row=4, column=3, rowspan=2, **sticky)
Button(frame, text='Clear', command=clear, **options).grid(row=1, column=0, **sticky)
#This will be used to run the program. 
win.mainloop()

