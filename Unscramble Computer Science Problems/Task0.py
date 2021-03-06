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

if __name__ == "__main__":
    text = texts[0] #O(1)
    call = calls[len(calls)-1] #O(1)

    print("First record of texts, {} texts {} at time {}".format(text[0],text[1],text[2])) #O(1)
    print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(call[0],call[1],call[2],call[3])) #O(1) 

"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

