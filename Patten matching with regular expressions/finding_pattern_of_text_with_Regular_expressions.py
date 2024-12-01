import re
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')

mo = phoneNumRegex.search('My phone number is 414-555-4242.')
print("Phone number found: " + mo.group())
print(mo.group(1))
print(mo.group(2))
print(mo.group(3))