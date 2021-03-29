print("Insert the text that, you want to learn the word count!")

text = input()

counts = dict()

names = text.split()

for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1

print(counts)