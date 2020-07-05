from datetime import datetime as dt

odds = [x for x in range(1, 60) if x % 2 == 1]
right_this_minute = dt.today().minute
if right_this_minute in odds:
    print("This minute seems a little odd.")
else:
    print("Not an odd minute.")
