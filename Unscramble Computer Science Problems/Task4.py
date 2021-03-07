"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


if __name__ == '__main__':
    incomingtext = []
    outgoingtext = []
    incomingcall = []
    outgoingcall = []
    telemarketers = set([])

    for text in texts: #O(n)
        outgoingtext.append(text[0])
        incomingtext.append(text[1])
    
    for call in calls: #O(n)
        outgoingcall.append(call[0])
        incomingcall.append(call[1])
    
    for x in outgoingcall: #O(n)
        if(not (x in outgoingtext or x in incomingtext or x in incomingcall)):#O(n)
            telemarketers.add(x) #O(1)
    print("These numbers could be telemarketers: ")
    for y in sorted(telemarketers): #O(n) + O(nlogn)
        print(y)


"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but 

never send texts,
receive texts or 
receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

