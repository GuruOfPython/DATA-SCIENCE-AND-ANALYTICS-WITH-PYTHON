import re

# 1. Amazon.com
str = "1-16 von 28 Ergebnissen oder Vorschlägen für "
match = re.findall(r'([0-9\-]+) von ([0-9]+)', str)
print(match[0][1])

# 2. Amazon.fr
str = "1-16 von 28 Ergebnissen oder Vorschlägen für "
match = re.findall(r'([0-9\-]+) von ([0-9]+)', str)
print(match[0][1])

# 3. Amazon.co.uk
str = "1-16 von 28 Ergebnissen oder Vorschlägen für "
match = re.findall(r'([0-9\-]+) von ([0-9]+)', str)
print(match[0][1])

# 4. Amazon.es
str = "1-16 von 28 Ergebnissen oder Vorschlägen für "
match = re.findall(r'([0-9\-]+) von ([0-9]+)', str)
print(match[0][1])

# 5. Amazon.it
str = "1-16 von 28 Ergebnissen oder Vorschlägen für "
match = re.findall(r'([0-9\-]+) von ([0-9]+)', str)
print(match[0][1])

# 6. Amazon.de
str = "1-16 von 28 Ergebnissen oder Vorschlägen für "
match = re.findall(r'([0-9\-]+) von ([0-9]+)', str)
print(match[0][1])