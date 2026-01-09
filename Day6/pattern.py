import re
text = "HELLO python123 12***34"
print(re.findall("\d",text))
print(re.findall("\D",text))
print(re.findall("\s",text))
print(re.findall("\S",text))
print(re.findall("\w",text))
print(re.findall("\W",text))
print(re.findall("\b",text))
print(re.findall("\B",text))

