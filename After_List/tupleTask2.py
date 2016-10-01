from operator import itemgetter,attrgetter              #Used in sort.

# inputArr = input("Enter Inputs:")
# print (inputArr);
#
# inputData = list(inputArr);     #Getting List of inputs.
# print ("Print Input Data");
# print (inputData);

#Hint : While loop & itemgetter

# inputArr = [];
# stopFlag = True;
# arrLength = 0;
#
# for inputData in inputArr:
#     tempArr = input("Enter Data");
#     inputArr.append(tempArr)
#     if arrLength ==  5:
#         arrLength = len(inputArr);
#
# print ("Input Data");
# print (inputArr)

#Sort with the help of lambda expressions.

students = [];
while True:
    name = input("Enter Name:");
    age = input("Enter Age:");
    height = input("Enter Height:");
    cont = input("Continue? :");
    students.append((name,age,height));

    if cont != 'Y':
        break;

print ("Sorted Students data")
print (sorted(students,key=itemgetter(0,1,2)));

#To check whether a value is in a lit or not use 'in' keyword after value.
# "mushroom" in mushroon_list
#Result : True (Assuming values is present in the list)
