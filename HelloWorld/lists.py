lists = ['trek', 'cannondale', 'redline', 'specialized'];

#traversing.
for list_element in lists :
    print ("List Element at indexes");
    print (list_element);

print()
tempLists = sorted(lists);
print ("Temp & Sorted list");
print (tempLists);

# message = "Hello Python world!"
#    print(message)             #Here Python tells us unnecessary Indent.

squares = []
if __name__ == '__main__':
    for value in range(1,11):
      square = value**2            #Square of numbers in range of 1-11
      squares.append(square)
      print(squares)

#Slicing a list
print ();
print ("Slicing a list");
players = ['charles', 'martina', 'michael', 'florence', 'eli'];
print(players[0:3]);              #Zero is Including Index where '3' is excluding Index.
print ("Slicing again");
print (players[:4]);