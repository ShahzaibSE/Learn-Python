import sys
print(sys.argv[1]);     #Params
numbers_List = [1,2,3,4,5,6,7,8,9,10];
FinalNum = [];

# print ("Numbers")
# print (numbers_List);

for num in numbers_List:
    if num % 2 !=0 :
        FinalNum.append(num**2);


print("Odd Number Squarred");
print(FinalNum);

#List Comprehension
value = 1;
# comprehentedList =  [value*2 for value in range(1,10)];

# for numComp in numbers_List:
#     if num % 2 !=0 :
#         comprehentedList.append([numComp*2 in numbers_List])

# x=1
# comprehentedList [x*2 in range(1,10)]
#
# print("Comprehented List");
# print(comprehentedList);

# counter = 0;
# limit = 11;
# while  counter < 11 :
#     print (numbers_List[counter]);
#     counter = counter + 1;


'''HomeWork
      Study & Implement List Comprehension
'''
odd_nums = [num**2 for num in range(1,4) if  num%2 !=0];       #List comhension task.
print("Odd numbers squared");
print (odd_nums);

test_numbers = [];
for insertNum in range(1,10,3):           #Third paramter is added in first parameter.
    test_numbers.append(insertNum);
    print (test_numbers);
