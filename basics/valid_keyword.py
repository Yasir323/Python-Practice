# HOW TO CHECK IF A STRING IS KEYWORD?

# importing "keyword" for keyword operations
import keyword

songs = "it starts with one thing i don't know why it doesn't even matter how hard you try keep that in mind i designed this rhyme to make in due time"

keys = songs.split(' ')
for i in range(len(keys)):
    if keyword.iskeyword(keys[i]):
        print(keys[i] + " is python keyword.")
    else:
        print(keys[i] + " is not a keyword.")
