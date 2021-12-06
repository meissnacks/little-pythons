#This will read through a mail log, build a histogram using a dictionary to count how many messages have come from each email address, and print the dictionary.
fileName = input('Enter a text file name: ')
try:
    fhand = open(fileName)
except:
    print('invalid file name')
    exit()
counts = dict()
for line in fhand:
    line = line.rstrip()
    if line.startswith('From '):
        #add the sender (the second word of the line) to the dictionary to keep a running count of who sent messages
        words = line.split()
        sender = words[1]
        counts[sender] = counts.get(sender, 0) +1
print(counts)

#This determines who has the most messages in the file. 

vals = list(counts.values())
print(vals)
maximum = max(vals)
print(maximum)

keys = list()
for key, value in counts.items():
    if value == maximum:
        print(key, value)


