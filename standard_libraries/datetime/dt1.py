from datetime import datetime
import time

dt = datetime(2020, 1, 1)   # year/month/date
dt1 = datetime.now()
dt2 = datetime.strptime("2020/01/01", "%Y/%m/%d")   # Converts string to datetime object
dt3 = datetime.fromtimestamp(time.time())
print(dt)
print(dt1)
print(dt2)
print(dt3)
print(f"{dt1.year}/{dt1.month}/{dt1.day}")
print(dt1.strftime("%Y/%m"))    # Convert datetime object to string
print(dt1 > dt2)
