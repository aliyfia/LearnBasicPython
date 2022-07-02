#  [start: stop: step]

DataInput = input("Enter your input and then ill slice this obj = ")
pDataInput = len(DataInput)
Space1 = DataInput.find(" ", 0, pDataInput)
Space2 = DataInput.find(" ", Space1+1, pDataInput)


Space1 = int(Space1)
Space2 = int(Space2)

print(DataInput)
print(Space1)
print(Space2)

slice1 = DataInput[0:DataInput.find(" ", 0, pDataInput)]
slice2 = DataInput[DataInput.find(" ", 0, pDataInput)+1:DataInput.find(" ", DataInput.find(" ", 0, pDataInput), pDataInput)]
slice3 = DataInput[DataInput.find(" ", DataInput.find(" ", 0, pDataInput)+1, pDataInput)+1:pDataInput]

print(slice1)
print(slice2)
print(slice3)
print(DataInput)
print(DataInput[::-1])
print(DataInput[::2])


