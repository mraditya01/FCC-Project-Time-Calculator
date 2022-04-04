def add_time(start, duration, days=""):
  #Splitting the time into two integer
  a=duration.split(":")
  b=start.split(" ")
  startTime=b[0].split(":")
  Initialh=int(startTime[0])
  Initialm=int(startTime[1])
  hour=int(a[0])
  days1 = ""
  elapsedDay=""
  #Adding the duration to the starting time and AP (AM and PM changes)
  (min2hour, new_min)=divmod((int(a[1])%60+Initialm),60)
  (AP,new_hour) = divmod((Initialh + hour + min2hour),12)
  if new_hour==0:
    new_hour=12
  #AM and PM changes
  daysGone=(Initialh + hour + min2hour)//24
  if AP == 0 or AP%2 == 0:
    AMPM=b[1]
  elif b[1] == "AM":
    AMPM="PM"
  elif b[1] == "PM":
    daysGone+=1
    AMPM="AM"
  #Adding Extra if More than days etc.
  daysd1={"Sunday":1,"Monday":2,"tuesday":3,"Wednesday":4,"Thursday":5,"Friday":6,"saturDay":7}
  if len(days) > 0:
    days1 = f", {days}"
    if days in daysd1:
      days1=(daysd1[days]+daysGone)%7
      daysd2 = {value: key for key, value in daysd1.items()}
      days1=f", {daysd2[days1]}"
  if daysGone > 1:
    elapsedDay = f" ({daysGone} days later)"
  elif daysGone == 1:
    elapsedDay = f" (next day)"
  #Return
  if len(str(new_min)) == 1:
    new_time=f"{new_hour}:0{new_min} {AMPM}{days1}{elapsedDay}"
  else:
    new_time = f"{new_hour}:{new_min} {AMPM}{days1}{elapsedDay}"

  return new_time