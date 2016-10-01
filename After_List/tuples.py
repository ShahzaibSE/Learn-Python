myTuple =  (1,"Shahzaib",2,"Leon");
print ("My Tuple");
print (myTuple);

#Lets try to edit value at 0 index.
# myTuple[0] = 4;
# print ("Trying to edit tuple")
# print (myTuple);

print("Traversing in tuples");
for items in myTuple:
    print("Tuple");
    print (items);

#We can online overwrite already created tuple.
newTuple = (1,"Chris",2,"Leon");
myTuple = newTuple;       #Here old tuple changed.
print ("First Tuple Changed");
print (myTuple);

convertedTuple = list(myTuple);
print("Tuple converted");
print (myTuple);

#Treating Converted Tuple into list.
convertedTuple[3] = "Jill";
print ("Tuple converted into list");
print (myTuple);
