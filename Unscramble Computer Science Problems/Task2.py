"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)



"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

if __name__ == '__main__':
    time = {}
    
    for call in calls: #O(n)
        if str(call[0]) in time:
            time[str(call[0])] = time[str(call[0])] + int(call[3]) #O(1)
        else:
            time[str(call[0])] = int(call[3]) # O(1)

        if str(call[1]) in time:
            time[str(call[1])] = time[str(call[1])] + int(call[3]) #O(1)
        else:
            time[str(call[1])] = int(call[3]) # O(1)

    max_key = max(time, key=time.get) #O(n)
    
    print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(max_key, time[max_key])) #O(1)
