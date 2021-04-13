import tkinter
from tkinter import *
from tkinter import messagebox

# setting up the tkinter window
root = tkinter.Tk()
root.geometry("250x400+450+200") #300 + 300 are coordinates such that it opens in middle
root.resizable(0,0) #therefore it cant be sized and rezied option will be disabled
root.title("Calculator(Amaan)")

val = ""
A = 0 #a is intializaed as integr variable with 0 value initially nd when u press + then integer gets converted into string
operator = "" 

# function for numerical button clicked

def btn_1_isclicked():
    global val # means val present in line 11
    val = val + "1" # val is global 
    data.set(val) # now the value of label is val

def btn_2_isclicked():
    global val
    val = val + "2"
    data.set(val)

def btn_3_isclicked():
    global val
    val = val + "3"
    data.set(val)

def btn_4_isclicked():
    global val
    val = val + "4"
    data.set(val)

def btn_5_isclicked():
    global val
    val = val + "5"
    data.set(val)

def btn_6_isclicked():
    global val
    val = val + "6"
    data.set(val)

def btn_7_isclicked():
    global val
    val = val + "7"
    data.set(val)

def btn_8_isclicked():
    global val
    val = val + "8"
    data.set(val)

def btn_9_isclicked():
    global val
    val = val + "9"
    data.set(val)

def btn_0_isclicked():
    global val
    val = val + "0"
    data.set(val)


# functions for the operator button click
def btn_plus_clicked():
    global A
    global operator,val
    A = int(val) #string (integer) gets converted into integer
    operator = "+"
    val = val + "+"
    data.set(val)

def btn_minus_clicked():
    global A
    global operator,val
    A = int(val)
    operator = "-"
    val = val + "-"
    data.set(val)

def btn_mult_clicked():
    global A
    global operator,val
    A = int(val)
    operator = "*"
    val = val + "*"
    data.set(val)

def btn_div_clicked():
    global A
    global operator,val
    A = int(val)
    operator = "/"
    val = val + "/"
    data.set(val)

def btn_c_pressed():
    global A,operator,val
    A = 0 # A = int(val) -- we cant use this since if then for first time when we click on c it will work fine but next time will give error since val variable a string with nothing b/w it(empty string) cant be converted into a integer type
    val = ""
    #operator = ""
    data.set(val)


# function to find the result
def result():
    global A,operator,val
    val2 = val
    if operator == "+":
        x = int((val2.split("+")[1])) #(val2.split("+")[1]) means splitting val2 on basis of + and getting value of string at index 1
        C = A + x ##a is intializaed as integr variable with 0 value initially nd when u press + then string integer gets converted into string
        val = str(C) #conversion to string necessary since ex 15+15=30 and then 30=c should be converted to string before further use since initially c is integer(floatiing)
        data.set(val)
    if operator == "-":
        x = int((val2.split("-")[1]))
        C = A - x
        val = str(C)
        data.set(val)
    if operator == "*":
        x = int((val2.split("*")[1]))
        C = A * x
        val = str(C)
        data.set(val)
    if operator == "/":
        x = int((val2.split("/")[1]))
        if x == 0:
            messagebox.showerror("Error", "Division By 0 Not Supported")
            C = 0 # C = A / x --> it is not possible since it will give division by 0 error
            val = str(C)
            data.set(val)
            
        else:
            C = int(A / x) #int since c will give value in floating no then
            val = str(C)
            data.set(C)


# the label that shows the result
data = StringVar() #intializating data variable that it is string variable
lbl = Label(
    root,
    text = "Label",
    anchor = SE,  #tells where our label should be , in south east
    font = ("Verdana", 20),
    textvariable = data,
    background = "#ffffff", #background colour different from button colours
    fg = "#000000", #foreground colour if black
)
lbl.pack(expand = True, fill = "both")

# the frames section
btnrow1 = Frame(root) #means this frame will consider root window as a parent window and (root, bg="##00000") u can also change colour like this
btnrow1.pack(expand = True, fill = "both") #expand true means it will expand if given chance and fill both means will fill both in expanding x  and y

btnrow2 = Frame(root)
btnrow2.pack(expand = True, fill = "both")

btnrow3 = Frame(root)
btnrow3.pack(expand = True, fill = "both")

btnrow4 = Frame(root)
btnrow4.pack(expand = True, fill = "both")
#each above frame will take equal space

# The buttons section
btn1 = Button( #its parent is frame(btnrow1) not root
    btnrow1,
    text = "1",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_1_isclicked,
)
btn1.pack(side = LEFT, expand = True, fill = "both",)

btn2 = Button(
    btnrow1,
    text = "2",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_2_isclicked,
)
btn2.pack(side = LEFT, expand = True, fill = "both",)

btn3 = Button(
    btnrow1,
    text = "3",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_3_isclicked,
)
btn3.pack(side = LEFT, expand = True, fill = "both",)

btnplus = Button(
    btnrow1,
    text = "+",
    font = ("Verdana", 22), #font size is 22
    relief = GROOVE,
    border = 0,
    command = btn_plus_clicked,
)
btnplus.pack(side = LEFT, expand = True, fill = "both",)

# buttons for frame 2

btn4 = Button(
    btnrow2,
    text = "4",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_4_isclicked,
)
btn4.pack(side = LEFT, expand = True, fill = "both",)

btn5 = Button(
    btnrow2,
    text = "5",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_5_isclicked,
)
btn5.pack(side = LEFT, expand = True, fill = "both",)

btn6 = Button(
    btnrow2,
    text = "6",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_6_isclicked,
)
btn6.pack(side = LEFT, expand = True, fill = "both",)

btnminus = Button(
    btnrow2,
    text = "-",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_minus_clicked,
)
btnminus.pack(side = LEFT, expand = True, fill = "both",)

# button for frame 3

btn7 = Button(
    btnrow3,
    text = "7",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_7_isclicked,
)
btn7.pack(side = LEFT, expand = True, fill = "both",)

btn8 = Button(
    btnrow3,
    text = "8",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_8_isclicked,
)
btn8.pack(side = LEFT, expand = True, fill = "both",)

btn9 = Button(
    btnrow3,
    text = "9",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_9_isclicked,
)
btn9.pack(side = LEFT, expand = True, fill = "both",)

btnmult = Button(
    btnrow3,
    text = "*",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_mult_clicked,
)
btnmult.pack(side = LEFT, expand = True, fill = "both",)

# button for frame4


btnc = Button(
    btnrow4,
    text = "C",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_c_pressed,
)
btnc.pack(side = LEFT, expand = True, fill = "both",)

btn0 = Button(
    btnrow4,
    text = "0",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_0_isclicked,
)
btn0.pack(side = LEFT, expand = True, fill = "both",)

btnequal = Button(
    btnrow4,
    text = "=",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = result,
)
btnequal.pack(side = LEFT, expand = True, fill = "both",)

btndiv = Button(
    btnrow4,
    text = "/",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_div_clicked,
)
btndiv.pack(side = LEFT, expand = True, fill = "both",)

root.mainloop()
