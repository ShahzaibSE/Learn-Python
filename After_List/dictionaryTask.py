'''
With a given integeral number n, write a program to generate a dictionary that contains (i,i*i) such that is an Integeral number
between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1:1 , : 4 ,4: 15, 5: 25 ,6: 36, 7: 49 , 8 :64}
'''


limit = int(input("Enter number:"));
myDictionary = {};
n = int(input("Enter Initial number:"));

for n in range(n,limit+1):      #We did increament of 1 in order to include limit.
   myDictionary[n] = n*n;

print ("My Dictionary");
print (myDictionary);

#To Captalize string use method 'title()'.
