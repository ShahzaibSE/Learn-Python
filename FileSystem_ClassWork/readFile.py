#File Exception.

try:
 with open('files/yFile') as fileObject:
     content = fileObject.read();
     print (content);

except FileNotFoundError:
    print("File not found");
