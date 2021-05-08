def to24h(time):
  (timeStr, ampm) = time.split(" ")
  (hourStr, minutesStr) = timeStr.split(":")
  
  hour = int(hourStr)
  minutes = int(minutesStr)
  
  if ampm == "PM":
    if hour != 12:
      hour = hour + 12
  else:
    if hour == 12:
      hour = 0

  return (hour, minutes)

def to12h(hour, minutes):
  ampm = "AM"
  if hour >= 12:
    ampm = "PM"
    hour = hour - 12
  if hour == 0:
    hour = 12

  return str(hour) + ":" + '{:02d}'.format(minutes) + " " + ampm
  

def parseDuration(duration):
  (hoursStr, minutesStr) = duration.split(":")
  days = 0
  hours = int(hoursStr)
  minutes = int(minutesStr)

  if hours >= 24:
    days = hours // 24
    hours = hours % 24

  return (days, hours, minutes)

def getDayOfWeek(startingDay, days):
  daysOfWeek = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
  for i, day in enumerate(daysOfWeek):
    if startingDay.lower() == day.lower():
      return daysOfWeek[(i + days) % len(daysOfWeek)]

def add_time(start, duration, startingDay=None):
  (startHour, startMin) = to24h(start)
  (days, hours, minutes) = parseDuration(duration)
  
  endMin = startMin + minutes
  if endMin >= 60:
    hours += 1
    endMin = endMin % 60

  endHour = startHour + hours
  if endHour >= 24:
    days = days + (endHour // 24)
    endHour = endHour % 24

  endingDay = None
  if startingDay != None:
    endingDay = getDayOfWeek(startingDay, days)

  newTime = to12h(endHour, endMin)
  if endingDay != None:
    newTime = newTime + ", " + endingDay
  if days > 0:
    if days == 1:
      newTime = newTime + " (next day)"
    else:
      newTime = newTime + " (" + str(days) + " days later)"

  return newTime