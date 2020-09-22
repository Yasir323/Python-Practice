import os
totalsize = 0
for filename in os.listdir('C:\\Windows\\System32'):
    totalsize += os.path.getsize(os.path.join('C:\\Windows\\System32', filename))

print(f'{totalsize}kB')
