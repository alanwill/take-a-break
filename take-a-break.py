import time
import webbrowser

total_breaks = int(raw_input("How many breaks would you like to take? "))
sleep_count = int(raw_input("What's your desired break length? (in seconds) "))
break_count = 0

print "take-a-break started on " + time.ctime()
while (break_count < total_breaks):
  time.sleep(sleep_count)
  webbrowser.open("http://www.youtube.com")
  break_count = break_count + 1

print "take-a-break ended on " + time.ctime()
