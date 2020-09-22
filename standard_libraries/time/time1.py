import time

print(time.time())
# Return the time in seconds since the epoch as a
# floating point number. The specific date of the
# epoch and the handling of leap seconds is platform
#  dependent. On Windows and most Unix systems, the
# epoch is January 1, 1970, 00:00:00 (UTC) and leap
# seconds are not counted towards the time in seconds
# since the epoch. This is commonly referred to as
# Unix time.
print(time.strftime("%H:%M:%S"))
print(time.strftime("%H %M %S"))
print(time.strftime("%A %p"))
