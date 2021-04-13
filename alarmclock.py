from playsound import playsound
from tkinter import * # here starts means import everything from tkinter
from win10toast import ToastNotifier
import datetime
import time

alarmsoundvalue = ""

def getvalue():
    set_alarm = f"{hour.get()}:{min.get()}:{sec.get()}"
    global alarmsoundvalue 
    alarmsoundvalue = f"{alarmsound.get()}"
    alarm(set_alarm)

def alarm(set_alarm):
    toast = ToastNotifier()
    while True: #infinite loop
        time.sleep(1) #run this loop after every one second and show current time
        date = datetime.datetime.now()
        now = date.strftime("%H:%M:%S") #time should be in this format(hour, minute , second)
        print(now)
        if now == set_alarm:
            print("Alarm Clock")
            toast.show_toast("Alarm Clock",duration=1) #if time reaches our time of alarm clock then show this notification within 1 second 
            playsound(alarmsoundvalue)

root = Tk()
root.title("Alarm Clock")
root.geometry("500x250")
info = Label(root,text = "(24)Hour  Min   Sec").place(x = 200, y = 30)
set_time = Label(root,text = "Set Time(24 hour format)",relief = "solid",font=("Cambria",10,"bold")).place(x = 45, y = 68) #relief solid means background border (black line)
file_path = Label(root,text = "Enter mp3 file path",relief = "solid",font=("Cambria",10,"bold")).place(x = 45, y = 93)

# Entry Variables
hour = StringVar() 
min = StringVar() 
sec = StringVar()
alarmsound = StringVar()

# Entry Widget
hour_E = Entry(root,textvariable = hour,bg = "grey",width = 4).place(x=210,y=70)
min_E = Entry(root,textvariable = min,bg = "grey",width = 4).place(x=240,y=70)
sec_E = Entry(root,textvariable = sec,bg = "grey",width = 4).place(x=270,y=70)
alarmsound_E = Entry(root,textvariable = alarmsound,bg = "grey",width = 20).place(x=210,y=100)
submit = Button(root,text = "Set Alarm",width = 10,command = getvalue).place(x =212,y=170) #command = getvalue it will take all entered value and getvalue function is defined in line 8

root.mainloop()

#alias error