DataInput = input("Please write your input = ")
LengthOfInput = len(DataInput)
IndexCharSpace = DataInput.find(" ")
IndexCharSpace2 = DataInput.find(" ", IndexCharSpace+1, LengthOfInput)
isAlpha = DataInput.isalpha()
isDigit = DataInput.isdigit()

print(DataInput)
print("Your Input is ", LengthOfInput, "Character Including the space")
print("Your First Space in index", IndexCharSpace, " Second Space is in Index", IndexCharSpace2)
print("Is your input alpha ?", isAlpha, "Is Your Input Digit ?", isDigit)


