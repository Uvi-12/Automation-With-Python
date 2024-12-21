"""Creating Regex Objects"""
import re
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')

"""Matching Regex Objects"""
mo = phoneNumRegex.search('My phone number is 414-555-4242.')
print("Phone number found: " + mo.group())

"""
Review of Regular Expression Matching
While there are several steps to using regular expressions in Python, each step is fairly simple.
-1. Import the regex module with import re.
-2. Create a Regex object with the re.compile() function. (Remember to use a raw string.)
-3. Pass the string you want to search into the Regex object’s search() method. This returns a Match object.
-4. Call the Match object’s group() method to return a string of the actual matched text.
"""

"""Grouping With Parenthesis"""
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
print("Phone number found: " + mo.group())
print(mo.group(0))
print(mo.group(1))
print(mo.group(2))
print(mo.group(3))

areaCode, mainNumber, lastDigits = mo.group(1), mo.group(2), mo.group(3)
print(areaCode)
print(mainNumber)
print(lastDigits)

#If the phone numbers you are trying to match have the area code set in parentheses. In this case, you need to escape the (and) characters with a backslash."""
phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My phone number is (415) 555-4242')
print(mo.group(1))
print(mo.group(2))

"""Matching multiple groups with the pipe"""
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
print(mo1.group())

mo2 = heroRegex.search('Tina Fey and Batman')
print(mo2.group())

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo3 = batRegex.search('Batmobile lost a wheel')
print(mo3.group())
print(mo3.group(1))

"""Optional matching with the Question Mark"""
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())

"""Matching zero or more with the star"""
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batwoman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())

mo3 = batRegex.search('The Adventures of Batwowowoman')
print(mo3.group())

"""Matching Specific Repetitions with Curly Brackets"""
haRegex = re.compile(r'(Ha){3}')
mo1 haRegex.search('HaHaHa')
print(mo1.group())

mo2 haRegex.search('Ha')
print(mo2 == None)
