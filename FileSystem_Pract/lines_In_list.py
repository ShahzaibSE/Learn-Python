with open('textFiles/py_digits2.txt') as fileObject:
    list_lines = fileObject.readline()

print("Lines in list");
for line in list_lines:
    print (line);

    #Looking for a letter or number.
    if(line == "3"):
        print ("Bit found");

