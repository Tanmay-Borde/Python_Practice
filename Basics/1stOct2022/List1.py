
values = [10,20,30,40]
print("List : ",values)
print("Type of the List : ",type(values))
print("Length of the List : ",len(values))
values.insert(2,11)
print("Index 0 : ",values[0])
print("Index 1 : ",values[1])
print("Index 2 : ",values[2])
print("Index 3 : ",values[3])
values.append(50)               # Inserting a value in the List
print("Index 4 : ",values[4])
values.remove(50)
print("List after deleting a value : ",values)
print(type(values[0]))
values.append(90.89)
print(values)
print(type(values[4]))
