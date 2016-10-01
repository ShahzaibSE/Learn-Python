'''
Write a program which accepts a sequence of comma-seperated numbers from console and generate a list and a tuple contains every number.
Suppose the following input is supplied to the program.
'''

# import sys
#
# inputs = [];
# for input_item in sys.argv():
#     inputs.append(input_item);
#
# print (inputs);

#http://stackoverflow.com/questions/7845165/how-to-take-input-in-an-array-python

numbers = input("Enter Inputs:");
numbers_list = numbers.split(',');
print ("Numbers List");
print (numbers_list);
print ("Numbers Tuple");
print (tuple(numbers_list));
print ("Numbers Length");
print (str(len(numbers_list)))