from datetime import datetime, timedelta, timezone



############ 1

current_datetime = datetime.now()

# print(current_datetime)

######### 2

# date = current_datetime - timedelta(days=15)
# print(date.strftime("%d/%m/%y"))

# time = current_datetime.time()
# print(time)
# print(time.strftime("%H:%M:%S"))

# "Jan 12, 2024"

# %b - month_name, %d day % dya_name, %y year

# formatted_date = date.strftime("%B %d, %Y")
# formatted_time = time.strftime("%I:%M %p")
# print(formatted_time)


############
# formatted_date = date.strftime("%B %d, %Y")
# print(formatted_date)

#########comparision
# date = current_datetime
# date1 = current_datetime + timedelta(hours=15)

# print(date1)

##########timezone

# utc_timezone = datetime.now()  #  you locations timezone
utc_timezone = datetime.now(timezone.utc)  #  from where the time is refrenced timezone  5:30 hours back

print(utc_timezone)
