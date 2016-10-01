message = "Hello World";
print (message);

message = "Hello Python World";
print (message);

print ("Another message");
print (message +" "+"Is this really python world?");

_message = "Hello again Python world again";
print(_message+" "+"Oh....yes this is python world alright");

mesage = "";
print(mesage);   #Here we omitted 's' from message

x=1;

if x==1 :
  print ("Expression meets");
  print (x);
else :
    print ("X is not equal to #1");

# switch x : {
#
# }

# Number to strings.

def number_to_string(arg):
    switcher = {
        0: "zero",
        1: "one",
        2: "two",
    }
    return switcher.get(arg,"Default case");

test_result_1 = number_to_string(0);
print ("Result of dictionary mapping"+" "+(test_result_1));

test_result_2 = number_to_string(3);                    #Where '3' is the key, which does not exist in dictionary
print ("Result of dictionary mapping"+" "+(test_result_2));

test_result_3 = number_to_string(3);                    #Where '3' is the key, which does not exist in dictionary
print ("Result of dictionary mapping"+" "+(test_result_3));

#Hello World.
print ("Hello World");
