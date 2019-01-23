import re

# 1. Amazon.com
str = "1-16 of 402 results for"
match = re.findall(r'([0-9\.\,]+) results', str)
print(match)

# 2. Amazon.fr
str = "1-16 sur 28 résultats pour"
match = re.findall(r'([0-9\.\,]+) résultats', str)
print(match)

# 3. Amazon.co.uk
str = "1-16 of 28 results for"
match = re.findall(r'([0-9\.\,]+) results', str)
print(match)

# 4. Amazon.es
str = "1-16 de más de 4.000 resultados para"
match = re.findall(r'([0-9\.\,]+) resultados', str)
print(match)

# 5. Amazon.it
str = "1-16 dei più di 4.000 risultati in"
match = re.findall(r'([0-9\.\,]+) risultati', str)
print(match)

# 6. Amazon.de
str = "1-16 von 28 Ergebnissen oder Vorschlägen für "
match = re.findall(r'([0-9\.\,]+) Ergebnissen', str)
print(match)