#http://www.secnetix.de/olli/Python/list_comprehensions.hawk      //List Comprehension Article.

import sys

insertNum = [];

for num in range(10):
    print (range(10));
    insertNum.append(num);
    print ("Number");
    print (insertNum);
# numbers = numbers.append(range(1,10));
# print ("Numbers");
# print (numbers);

noprimes = [j for i in range(2, 8) for j in range(i * 2, 10, i)]
print ("Non-prime numbers");
print (noprimes);

#Test Numbers.
test_num  = [];
counter = 0;
for i in range(2, 8):
    test_num.insert(counter,i);
    counter += 1;
print ("Test Numbers");
print (test_num);
