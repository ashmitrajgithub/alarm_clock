import tkinter as tk
from tkinter import *
from tkinter import messagebox
import os, time
import pygame
from threading import Thread
import datetime

def createwidgets():
    label1 = Label(root, text="Enter the time in hh:mm- ")
    label1.grid(row=0, column=0, padx=5, pady=5)

    global entry1
    entry1 = Entry(root, width=15)
    entry1.grid(row=0, column=1)

    label2 = Label(root, text="Enter the message of alarm: ")
    label2.grid(row=1, column=0, padx=5, pady=5)

    global entry2
    entry2 = Entry(root, width=15)
    entry2.grid(row=1, column=1)

    but = Button(root, text="submit", width=10, command=submit)
    but.grid(row=2, column=1)

    global label3
    label3 = Label(root, text="")
    label3.grid(row=3, column=0)

def message1():
    global entry1, label3
    Alarmtimelabel = entry1.get()
    label3.config(text="The Alarm is counting....")
    messagebox.showinfo("Alarm clock", f"The Alarm time is: {Alarmtimelabel}")

def check_alarm():
    global entry1, entry2, label3
    while True:
        current_time = time.strftime("%H:%M")
        alarm_time = entry1.get()
        if current_time == alarm_time:
            pygame.mixer.init()
            pygame.mixer.music.load("/Users/ashmitraj/Downloads/VisualCode/AlarmClock/123.mp3") #replace this path with your path
            pygame.mixer.music.play()
            label3.config(text="Alarm sound playing>>>>>")
            messagebox.showinfo("Alarm Message", f"The Message is: {entry2.get()}")
            pygame.mixer.quit()
            break

def submit():
    message1()
    label3.config(text="Alarm scheduled...")
    alarm_thread = Thread(target=check_alarm)
    alarm_thread.start()

root = tk.Tk()
root.title("Alarm Clock")
root.geometry("400x100")

createwidgets()

root.mainloop()
