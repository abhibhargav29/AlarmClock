from tkinter import Tk,Label,Entry,Button,StringVar,Frame
from tkinter.ttk import Combobox
from datetime import datetime
from time import strftime,sleep
from playsound import playsound

def time():
    string = strftime("%H:%M:%S %p")
    label1.configure(text = string)
    label1.after(1000, time)

def ringAlarm(alarm_time):
    i=0
    while(True):
        sleep(1)
        time()
        current_time = datetime.now()
        now = current_time.strftime("%H:%M:%S")
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
        if(now==alarm_time):
            msg.configure(text="WAKE UP!")
            playsound("alone_marshmello.mp3")
            break

def setAlarm():
    H = hourVar.get()
    M = minVar.get()
    S = secVar.get()
    try:
        if(int(H)<0 or int(H)>24):
            msg.configure(text="Enter correctly")
            clock.update()
            return
        elif(int(M)<0 or int(M)>=60):
            msg.configure(text="Enter correctly")
            clock.update()
            return
        elif(int(S)<0 or int(S)>=60):
            msg.configure(text="Enter correctly")
            clock.update()
            return
    except:
        msg.configure(text="Enter correctly")
        clock.update()
        return
    alarm_time = f"{H}:{M}:{S}"
    ringAlarm(alarm_time)

clock = Tk()
clock.title("Alarm Clock")
clock.geometry("500x200")
clock.configure(bg = "grey")

label1 = Label(clock, font=("Calibri",20), background="black", foreground="white")
label1.pack(fill="x")

L1 = Label(clock, text = "Hour : Min : Sec", font=30)
L1.pack()

hourVar = StringVar()
minVar = StringVar()
secVar = StringVar()

hour = Entry(clock, textvariable=hourVar, width=3, font=("Calibri",17), justify="center")
hour.place(x=176, y=73, height=25)

minute = Entry(clock, textvariable=minVar, width=3, font=("Calibri",17), justify="center")
minute.place(x=230, y=73, height=25)

second = Entry(clock, textvariable=secVar, width=3, font=("Calibri",17), justify="center")
second.place(x=284, y=73, height=25)

msg = Label(clock, text="", font=30, bg="grey")
msg.place(x=194, y=150)

button = Button(clock, text="OK", command=setAlarm)
button.place(x=283, y=103, width=45, height=25)

time()
clock.mainloop()
