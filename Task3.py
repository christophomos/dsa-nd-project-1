"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

from enum import auto, Enum

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


class PhoneType(Enum):
    Fixed = auto()
    Mobile = auto()
    Marketer = auto()


fixed_prefix = '('
bangalore_code = '080'
marketer_prefix = '140'


def parse_fixed_line(phone_number):
    return phone_number.split(')')[0][1:]


def classify_and_fetch_code(phone_number):
    if phone_number[0] == fixed_prefix:
        code = parse_fixed_line(phone_number)
        return PhoneType.Fixed, str(phone_number[1:4])
    elif phone_number[0:3] == marketer_prefix:
        return PhoneType.Marketer, marketer_prefix
    else:
        return PhoneType.Mobile, phone_number[0:4]

calls_from_bangalore = 0
calls_from_bangalore_to_bangalore = 0
codes_called_from_bangalore = set()


def is_bangalore(phone_type, code):
    return (phone_type == PhoneType.Fixed) and (code == bangalore_code)


for call in calls:
    caller = call[0]
    receiver = call[1]
    caller_type, caller_code = classify_and_fetch_code(caller)
    receiver_type, receiver_code = classify_and_fetch_code(receiver)
    if is_bangalore(caller_type, caller_code):
        calls_from_bangalore += 1
        codes_called_from_bangalore.add(receiver_code)
        if is_bangalore(receiver_type, receiver_code):
            calls_from_bangalore_to_bangalore += 1

assert parse_fixed_line('(6788) 478-2444') == '6788'
assert parse_fixed_line('(6) 478-2444') == '6'

print("The numbers called by people in Bangalore have codes:")
for code in sorted(list(codes_called_from_bangalore)):
    print(code)

percentage = calls_from_bangalore_to_bangalore / calls_from_bangalore * 100
print(f"{percentage:4.4} percent of calls from fixed lines in Bangalore are calls "
      f"to other fixed lines in Bangalore.")
