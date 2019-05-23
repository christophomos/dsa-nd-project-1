"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
from collections import defaultdict

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
call_time_dict = defaultdict(int)
for call in calls:
    caller = call[0]
    receiver = call[1]
    duration = int(call[3])
    for number in [caller, receiver]:
        call_time_dict[number] += duration

max_call_number = ""
max_call_length = 0
for number in call_time_dict:
    current_call_length = call_time_dict[number]
    if current_call_length > max_call_length:
        max_call_number = number
        max_call_length = current_call_length

print(f"{max_call_number} spent the longest time, {max_call_length} seconds, on the phone during September 2016.")

assert max_call_number == "(080)33251027"
assert max_call_length == 90456
