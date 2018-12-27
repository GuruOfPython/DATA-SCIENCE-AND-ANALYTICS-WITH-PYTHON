from nameparser import HumanName
name = HumanName("Ralf Mühlenhöver, Geschäftsführer")

print(name.title)
print(name.first)
print(name.middle)
print(name.last)