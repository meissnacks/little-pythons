#Exercise 3: Write a program to read through a mail log, build a histogram using a dictionary to count how many messages have come from each email address, and print the dictionary.
fileName = input('enter a txt file name, plz: ')
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

#Exercise 4: Add code to the above program to figure out who has the most messages in the file. After all the data has been read and the dictionary has been created, look through the dictionary using a maximum loop (see Chapter 5: Maximum and minimum loops) to find who has the most messages and print how many messages the person has.

vals = list(counts.values())
print(vals)
maximum = max(vals)
print(maximum)

keys = list()
for key, value in counts.items():
    if value == maximum:
        print(key, value)


