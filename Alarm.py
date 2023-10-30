from threading import Thread
from tkinter.ttk import *
from tkinter import *
import tkinter as tk

from PIL import ImageTk,Image 
from pygame import mixer
from datetime import datetime
from time import sleep


#color
bg_color = '#ffffff' 
col='#0344ff' #blue
co2='#ffffff' #red


#window

window =  Tk()
window.title("")
window.geometry('450x200')
window.configure(bg= bg_color)


#frame
Frame_line = Frame(window, width=500, height=5,bg=col)
Frame_line.grid(row=0,column=0)

Frame_body = Frame(window, width=500, height=300,bg=co2)
Frame_body.grid(row=1,column=0)

#frame body
img = Image.open('alarm-clock.png')
img.resize((500,200))
img = ImageTk.PhotoImage(img)
app_image= Label(Frame_body,height=100, image=img,bg=bg_color)
app_image.place(x=30,y=20)

name = Label(Frame_body, text = 'Alarm', height=1, font=('Ivy 18 bold'),bg=bg_color)
name.place(x=200,y=10)

hour = Label(Frame_body, text = 'Hour', height=1, font=('Ivy 10 bold'),bg=bg_color,fg=col)
hour.place(x=202,y=40)

c_hour=Combobox(Frame_body,width=2,font=('timenewromman 15'))
c_hour['values'] = ("00","01","02","03","04","05","06","07","08","09","10","11","12",)
c_hour.current(0)
c_hour.place(x=205,y=60)

min = Label(Frame_body, text = 'Minute', height=1, font=('Ivy 10 bold'),bg=bg_color,fg=col)
min.place(x=260,y=40)

c_min=Combobox(Frame_body,width=2,font=('timenewromman 15'))
c_min['values'] = ("00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60",)
c_min.current(0)
c_min.place(x=262,y=60)


sec = Label(Frame_body, text = 'Second', height=1, font=('Ivy 10 bold'),bg=bg_color,fg=col)
sec.place(x=317,y=40)

c_sec=Combobox(Frame_body,width=2,font=('timenewromman 15'))
c_sec['values'] = ("00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60",)
c_sec.current(0)
c_sec.place(x=320,y=60)


period= Label(Frame_body, text = 'Period', height=1, font=('Ivy 10 bold'),bg=bg_color,fg=col)
period.place(x=377,y=40)

c_period=Combobox(Frame_body,width=3,font=('timenewromman 15'))
c_period['values'] = ("AM","PM")
c_period.current(0)
c_period.place(x=380,y=60)

def activete_alarm():
    t =Thread (target=alarm)
    t.start()

def deactivete_alarm():
    print('Deactivate alarm :',selected.get())
    mixer.music.stop()

selected = IntVar

rad1=Radiobutton(Frame_body,font=('arial 10 bold'), value=1, text="Activate", bg=bg_color, command=activete_alarm, variable=selected)
rad1.place(x=200,y=100)


def sound_alarm():
    mixer.music.load('alarm-music.mp3')
    mixer.music.play()  
    selected.set(0)

rad2=Radiobutton(Frame_body,font=('arial 10 bold'), value=2, text="Deactivate", bg=bg_color, command=deactivete_alarm, variable=selected)
rad2.place(x=280,y=100)



def alarm():
    while True:
        control = 1
        print(control)

        alarm_hour=c_hour.get()
        alarm_minute =c_min.get()
        alarm_sec=c_sec.get()
        alarm_period=c_period.get()
        alarm_period = str(alarm_period).upper()
       
        now = datetime.now()

        hour   = now.strftime("%I") 
        minute = now.strftime("%M")
        second = now.strftime("%S")
        period = now.strftime("%p")

        if control == 1 :
            if alarm_period == period :
                if alarm_hour == hour:
                    if alarm_minute == minute :
                        if alarm_sec == second :
                            print("time to take a break!")
                            sound_alarm()
        sleep(1) 




mixer.init() 

window.mainloop()


