# with open('textFiles/py_digits2.txt') as file_object:      #Accessing file from a directory (Linux & OS X Format), here is forward slash
if __name__ == '__main__':
    with open('textFiles\py_digits2.txt') as file_object:        #Accessing file from a directory (Windows Format), here is back slash
        # content = file_object.read();
        # content = file_object.close();
        # print (content);
        print ("Reading file line by line");

        for line in file_object:
            # print (line);
            print(line.rstrip()); #trying to remove blank lines.
            #Finding a word in a file.
            if (line == "8979323846"):
                print("Word found");
