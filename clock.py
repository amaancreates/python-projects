import sys
from  tkinter import *
import time 

def times():
	current_time=time.strftime("%H:%M:%S") 
	clock.config(text=current_time)
	clock.after(200,times) #Means it will wait 200 milliseconds and then call times function
	
root=Tk()
root.geometry("500x250")
root.title("ALARM CLOCK (Amaan)")
clock=Label(root,font=("helvetica",50,"bold"),bg="YELLOW")
clock.place(x=110,y=70)
#clock.grid(row=2,column=2,pady=25,padx=100)
times()

digi=Label(root,text="Digital clock",font="times 24 bold")
digi.place(x=150, y= 160)
#digi.grid(row=0,column=2)

nota=Label(root,text="hours   minutes   seconds   ",font="times 15 bold")
nota.place(x=140, y=200)
#nota.grid(row=5,column=2)

root.mainloop()

