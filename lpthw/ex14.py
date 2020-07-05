from sys import argv
from os.path import exists

script, source, target = argv
print(f"Copying from {source} to {target}....")

#We can do these two in one line: indata = open(source).read()
#If we follow the approach above we don't need to close the file.
#It should already be closed by Python once that line runs.
in_file = open(source)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long.")

print(f"Does the output file exist? {exists(target)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()
#Again in one line it'd be: open(target).write(indata)
out_file = open(target, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()
