import webbrowser
import time

#Counters to control loop - repeat
total_break = 3
break_count = 0

#print a message on screen
print("This program started on " + time.ctime())

while(break_count < total_break):
    time.sleep(10)
    webbrowser.open("http://www.youtube.com")
    break_count = break_count+1
