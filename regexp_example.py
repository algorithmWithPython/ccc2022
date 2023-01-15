import re

string = "abc+123"
match = re.match("([a-zA-Z]+)([+-])([0-9]+)", string)
alphabetical_part = match.group(1)
sign = match.group(2)
numeric_part = match.group(3)

print(alphabetical_part, sign, numeric_part)
