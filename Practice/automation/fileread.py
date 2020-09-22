# Open the file
f = open("ex.txt", "r")
# Read it
# for line in f:
#     print(line, end='')
    # The file already has a newline char at the end
    # of every line

# Print only the ones who passed
for line in f:
    line_split = line.split()
    if line_split[2] == "P":
        print(line)
f.close()
