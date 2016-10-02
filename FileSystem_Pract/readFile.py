# with open('textFiles/py_digits2.txt') as file_object:      #Accessing file from a directory (Linux & OS X Format), here is forward slash
with open('textFiles\py_digits2.txt') as file_object:        #Accessing file from a directory (Windows Format), here is back slash
    content = file_object.read();
    # content = file_object.close();
    print (content);
    print ("File Abosolute path");
    print ("D:\PROJECTS\Python_Pract\FileSystem_Pract\readFile.py");