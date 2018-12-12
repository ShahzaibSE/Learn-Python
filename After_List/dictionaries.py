sample_dictionaries = {'name':"Shahzaib",'age':23};
#
# #Accessing different keys data from sample dictionary.
# print ("Person's name:"+" "+sample_dictionaries['name']);
# print ("Person's age:"+" "+str(sample_dictionaries['age']));
#
# #Adding new key.
# sample_dictionaries['gender'] = "Male";
# #Dictionary with new key.
# print ("Dictionary with new key");
# print (sample_dictionaries);
#
# #Editing sample_dictionaries name.
# sample_dictionaries['name'] = "Leon";
# print ("Sample Dictionary name changed");
# print (sample_dictionaries);
#
# print ();
# new_sample_dictionary = {1:"Leon",2:"Ada",3:"Chris",4:"Jill"};
# print ("Dictionary with numeric keys");
# print ("First Name:"+" "+new_sample_dictionary[1]);
# print ("Second Name:"+" "+new_sample_dictionary[2]);
# print ("Third Name:"+" "+new_sample_dictionary[3]);
# print ("Fourth Name:"+" "+new_sample_dictionary[4]);

print ();
#Traversing dictionary.
for k , v in sample_dictionaries.items():
    print ("Key:"+" "+k);
    print ("Value:"+" "+str(v));

print ();
# Traversing dictionary for keys.
for k in sample_dictionaries.keys():
    print ("Key:"+" "+k);
    # print ("Value:"+" "+str(v));

print ();
# Traversing dictionary for values.
for v in sample_dictionaries.values():
    # print ("Key:"+" "+k);
    print ("Value:"+" "+str(v));

print();
print(sample_dictionaries.fromkeys(sample_dictionaries,"Shahzaib"));
