from pprint import pprint

sentence = "This is a common interview question."
char_freq = {}
for char in sentence:
    if char.upper() in char_freq or char == ' ':
        continue
    else:
        counter = 0
        for char_rep in sentence:
            if char.lower() == char_rep.lower():
                counter += 1
        char_freq[char.upper()] = counter
pprint(char_freq, width=1)
print("Sorting")
pprint(sorted(char_freq.items(), key=lambda kv: kv[1], reverse=True), width=10)
print("The answer to pur problem:")
most_freq_char = sorted(char_freq.items(), key=lambda kv: kv[1], reverse=True)[0]
print(f"MOst frequently used character is: {most_freq_char[0]} and it is used {most_freq_char[1]} times.")
