# print (5/0);

#Using Divide by zero exception.

try :
   # with open('sample.txt') as fileObject:    #This line throws 'File not found exception'.
   with open('sample') as fileObject:
        print (fileObject.readlines());
   print(5 / 1);           #This will let else block to be executed.
   # print(5 / 0);         #This line will not let else block to be executed.
except ZeroDivisionError:
    print("You cannot divide by zero");
except FileNotFoundError:
    print ("File not found");
else:                 #Handling else block
    print ("Code executed successfully");
finally:
    print ("Execute code anyway");

    #Open the file again.
    with open('sample','a') as newfileObject:
        newfileObject.write("\nI love programming");