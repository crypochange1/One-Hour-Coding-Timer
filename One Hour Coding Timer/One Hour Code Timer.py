import time
import sys
from playsound import playsound
from tkinter import messagebox
from threading import Thread

def run_timer(seconds):
    for remaining in range(seconds, 0, -1):
        #Previous print version, no need for sys anymore to be honest
        #sys.stdout.write("\r")
        minutes = 0
        seconds = remaining
        if remaining > 60:
            minutes = int(seconds/60)
            seconds = int(seconds%60)
        else:
            seconds = remaining
        print("\r{:2d} minutes {:2d} seconds remaining.".format(minutes,seconds), flush = True, end="")
        #Also from previous version, no need for sys but a good refernce
        #sys.stdout.write("{:2d} minutes {:2d} seconds remaining.".format(minutes,seconds)) 
        #sys.stdout.flush()
        time.sleep(1)
    print("\rTime is up!") 
    if __name__ == '__main__':
        Thread(target = playsound('C:\Windows\Media\Alarm01.wav')).start()
        Thread(target = messagebox.showinfo("Alert", "Your one hour coding is done! Good Job fella!")).start()
        
#Start Timer
input("Press enter to start one hour timer...")
#place the amount of seconds you want in the timer function brackets()
run_timer(3600)#)