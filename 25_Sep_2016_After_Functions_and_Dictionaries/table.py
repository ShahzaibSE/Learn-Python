# Generate a table.

def generateTable(tableNum=2):
    print ("Table");
    for num in range(1,11):
        print (tableNum * num);
    return;

#Generating table.
generateTable();
print ("Another Table");
generateTable(5);

# testnum1 = 3;
# testnum2 = 4;
# result = testnum1 * testnum2;
#
# print ("Test Statement");
# print (testnum1+"x"+testnum2+"="+result);
#
# a = 3;
# b = 4;
#
# def sum(num1,num2):
#     num1.append(40);
#     num2 = 80;
#     return num1+num2;
#
# resultSum=sum();
# print("Addition:"+" "+resultSum);
#
# #Reference parameters.
# print("A:"+" "+a);
# print("B:"+" "+b);

a = [10,20];
b = 40;

def sum(num1,num2):
    num1.append(30);
    num1 = [40,50,60]
    num1.append(70);
    num2 = 50;
    return;

sum(a,b);
print ("A list")
print (a);
print ("B Value");
print (b);