#The time module provides a function, also named time, that returns the currentGreenwich Mean Time in “the epoch”, which is an arbitrary time used as a reference point. On UNIX systems, the epoch is 1 January 1970.
import time

stamp = time.time()


#Write a script that reads the current time and converts it to a time of day in hours, minutes, and seconds, plus the number of days since the epoch.

def humanTime(stamp):

  year =int( 1970 + stamp// 31556926)
  month =int( 1 + stamp%31556926//2629743)
  day = int(1 + stamp%2629743//86400)
  hour = int((stamp % 86400) //3600)
  minute = int(stamp%3600//60)
  sec = int(stamp%60)
  print("Today is  " + str(day) +"/"+ str(month) +"/"+ str(day) +"   "+ str(hour) + ":"+ str(minute) + ":"+ str(sec) )
humanTime(stamp)