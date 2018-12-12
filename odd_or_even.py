def checkNum(num):     #Checking whether number is odd or even
    if num % 2 == 0:
        return "Number is even"
    elif num % 2 != 0:
        return "Number is odd"

input_number = int(input('Enter your number:'));
result = checkNum(input_number);
print(result);