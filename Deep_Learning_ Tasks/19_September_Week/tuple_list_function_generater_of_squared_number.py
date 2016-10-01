def myfunction (param):
    print ("Param");
    print (param);
    return;

myfunction(5);

squaredNums = [];

#Function to generate squarred numbers.
def generate_SquaredTuple(list):
    for nums in range(1,21):       #range set 1 to 20 where 21 is excluding number.
        list.append(nums**2);     #Squared numbers in the list.
    tupleSquared_num = tuple(list)   #Converting squared number list into tuple.
    return tupleSquared_num;

#Catching squard number tuple
squaredNums = generate_SquaredTuple(squaredNums);
print ("Square numbers");
print (squaredNums);