"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import collections

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""


class SuspectInfo:
    made_outgoing_call = False
    removed_from_suspicion = False

    def __init__(self, removed_from_suspicion=False):
        self.removed_from_suspicion = removed_from_suspicion

    def is_suspect(self):
        return self.made_outgoing_call and not self.removed_from_suspicion


# By default, every outgoing phone number is suspicious - we remove it from suspicion if
# it sends a text, receives a text or receives an incoming phone call
# Maps every phone number to a SuspectInfo entry
suspect_dict = {}

marketer_prefix = '140'


def add_to_suspect_dict_if_needed(number, suspect_dict):
    if number not in suspect_dict:
        # Honest telemarketers removed from suspicion
        removed_from_suspicion = (number[0:3] == marketer_prefix)
        suspect_dict[number] = SuspectInfo(removed_from_suspicion)


for call in calls:
    caller = call[0]
    receiver = call[1]
    for number in [caller, receiver]:
        add_to_suspect_dict_if_needed(number, suspect_dict)
    suspect_dict[caller].made_outgoing_call = True
    # Receiver removed from suspicion since received a phone call
    suspect_dict[receiver].removed_from_suspicion = True

for text in texts:
    sender = text[0]
    receiver = text[1]
    for number in [sender, receiver]:
        if number in suspect_dict:
            suspect_dict[number].remove_from_suspicion = True

suspect_list = []

# Locate any suspect that wasn't removed from suspicion
for suspect_key in suspect_dict:
    entry = suspect_dict[suspect_key]
    if entry.is_suspect():
        suspect_list.append(suspect_key)

for suspect in sorted(suspect_list):
    print(suspect)
