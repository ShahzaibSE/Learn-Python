numbers = [];
i=0;

#Loop
for number in range (2000, 3200) :
 if (number % 7 == 0) and (number % 5 != 0) :
 	numbers.insert(i,number);
 	i=+1

print("Numbers pushed/Inserted");
print (numbers);
total_numbers_in_list = len(numbers);
print ("Type of total_numbers_in_list");
print(type(total_numbers_in_list));
print ("Numbers");
print (numbers);
print ("Total Numbers :"+" "+str(total_numbers_in_list));
print ("Using _len_ for finding length");
print(numbers.__len__());

#Boolean Value.
Boolean_test = True;
print ("Boolean Test");
print (Boolean_test);

