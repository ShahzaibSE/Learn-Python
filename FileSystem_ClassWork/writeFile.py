#Writing to a files.
# with open('files/myFile.txt','w') as file_object:
#     file_object.write("I love programming\n");
#     file_object.write("I really love programming\n");
#     # content = file_object.readable()
#     # print("Files Content");
#     # print(content);

#Opening a file in both read & write mode.
with open('files/myFile.txt','r+') as file_object:
    file_object.write("I love programming\n");
    file_object.write("I really love programming\n");
    content = file_object.read()
    print("Files Content");
    print(content);

