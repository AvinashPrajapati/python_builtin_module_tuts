# from datetime import timedelta, timezone
###in django :: from django.utils import timezone

# utc_timezone = timezone(timedelta(hours=5))

# print(utc_timezone)

###############
import time

currentTime  = time.time()
localTime  = time.localtime(currentTime)
# print(localTime)

#foramat
formattedTime = time.strftime("%d/%m/%Y, %I:%M:%S %p", localTime)

startTime = time.time()
time.sleep(3)
endTime = time.time()


sec = startTime - endTime
print(sec)
