DataString = "this is data where user input"

print(len(DataString))
x = DataString.find("i")
y = DataString.find("i", x+1, len(DataString))
z = DataString.find("i", y+1, len(DataString))


print(DataString)
print(x, y, z)
print(DataString.upper())
print(DataString.lower())
print(DataString.capitalize())
print(DataString.isdigit())
print(DataString.isalpha())

