"""import re
pattern = "Jayesh"
text = "Hello, my name is Jayesh and I love programming."
match = re.match(pattern, text)
if match:
    print("Match found!",match.group())
else:
    print("No match found.")"""

import re
pattern = "Jayesh"
text = "Hello, my name is Jayesh and I love programming."
result = re.search(pattern, text)
if result:
    print(" found!",result.group())
else:
    print("No found.")