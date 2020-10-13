from tkinter import *
from tkinter.ttk import Combobox
from datetime import datetime
from time import strftime,sleep
from playsound import playsound

#Active Clock
def time():
    string = strftime("%H:%M:%S")
    label1.configure(text = string)
    label1.after(1000, time)

#Alarm loop function
def ringAlarm(alarm_time):
    i=0
    while(True):
        sleep(1)
        
        #Active Clock
        time()
        
        #In case cancel button is pressed
        if(cancelVar.get()):
            msg["text"] = "Cancelled"
            print("................")
            clock.update()
            break
        
        #Get current time
        current_time = datetime.now()
        now = current_time.strftime("%H:%M:%S")
        
        #Loading/Working Effect
        print("Alarm Working")
        if(i%4==0):
            msg["text"] = "Alarm Set"
            clock.update()
        elif(i%4==1):
            msg["text"] = "Alarm Set."
            clock.update()
        elif(i%4==2):
            msg["text"] = "Alarm Set.."
            clock.update()
        else:
            msg["text"] = "Alarm Set..."
            clock.update()
        i+=1
        
        #Alarm Time
        if(now==alarm_time):
            msg.configure(text="WAKE UP!")
            file = songVar.get()
            playsound(file)
            print("................")
            break

#Alarm setter and validator
def setAlarm():
    H = hourVar.get()
    M = minVar.get()
    S = secVar.get()
    
    #Validate
    try:
        if(int(H)<0 or int(H)>24):
            msg.configure(text="Invalid Time")
            clock.update()
            return
        elif(int(M)<0 or int(M)>=60):
            msg.configure(text="Invalid Time")
            clock.update()
            return
        elif(int(S)<0 or int(S)>=60):
            msg.configure(text="Invalid Time")
            clock.update()
            return
    except:
        msg.configure(text="Invalid Time")
        clock.update()
        return
    
    #Ring Alarm
    alarm_time = f"{H}:{M}:{S}"
    cancelVar.set(False)
    ringAlarm(alarm_time)

#Cancel function
def cancelAlarm():
    cancelVar.set(True)
    
    
#Main Window
#basic
clock = Tk()
clock.title("Alarm Clock")
clock.geometry("500x200")
clock.configure(bg = "grey")

#Time Label
label1 = Label(clock, font=("Calibri",20), background="black", foreground="white")
label1.pack(fill="x")

#Hour min sec label
L1 = Label(clock, text = "Hour : Min : Sec", font=30)
L1.pack()

#Variables
hourVar = StringVar()
minVar = StringVar()
secVar = StringVar()
cancelVar = BooleanVar()
cancelVar.set(False)
songVar = StringVar(clock, value="alone_marshmello.mp3")

#Entry of variables
hour = Entry(clock, textvariable=hourVar, width=3, font=("Calibri",17), justify="center")
hour.place(x=176, y=73, height=25)

minute = Entry(clock, textvariable=minVar, width=3, font=("Calibri",17), justify="center")
minute.place(x=230, y=73, height=25)

second = Entry(clock, textvariable=secVar, width=3, font=("Calibri",17), justify="center")
second.place(x=284, y=73, height=25)

#Song Entry
song = Entry(clock, textvariable=songVar, font=("Calibri",10))
song.place(x=176, y=103, height=24, width=100)

#Result
msg = Label(clock, text="", font=30, bg="grey")
msg.place(x=196, y=155)

#Ok button
button = Button(clock, text="OK", command=setAlarm)
button.place(x=283, y=103, width=45, height=25)

#Cancel Button
cancelButton = Button(clock, text="CANCEL", command=cancelAlarm)
cancelButton.place(x=248, y=132, width=80, height=25)

#Active Clock
time()

#main window loop
clock.mainloop()
