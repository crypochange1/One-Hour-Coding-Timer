import time
import sys
from playsound import playsound
from tkinter import messagebox
from threading import Thread

def run_timer(seconds):
    for remaining in range(seconds, 0, -1):
        minutes = 0
        seconds = remaining
        if remaining > 60:
            minutes = int(seconds/60)
            seconds = int(seconds%60)
        else:
            seconds = remaining
        print("\r{:2d} minutes {:2d} seconds remaining.".format(minutes,seconds), flush = True, end="")
        time.sleep(1)
    print("\nTime is up!", flush = True, end="                \r") 
    if __name__ == '__main__':
        playsound('C:\Windows\Media\Alarm01.wav')
        messagebox.showinfo("Alert", "Your one hour coding is done! Good Job fella!")
        
#Start Timer
input("Press enter to start one hour timer...")
#Place the amount of seconds you want in the timer function brackets()
run_timer(3)#)