#Generate Two Dimensional Array.

#Params.
x=1;
y=1;

count1=0;
count2=0;

TwoDimensional_Array = [];
innerList = [];

# for num in range(1,100):
#     i = num;
#     j = num;
#     result = i*j;
#     TwoDimensional_Array.insert(i,innerList.insert(j,result));


for num1 in range(1,3) :
    i = num1
    for num2 in range(1,5) :
        j = num2;
        result = i*j;
        innerList.append(result);
    TwoDimensional_Array.append(innerList);
#         count2 =+1;
# count1 =+1;

print (TwoDimensional_Array);


# temp_x = 2;
# temp_y = 2;
# print(temp_x * temp_y);
#
# tempArr = [];
# tempArr[0][0] = 1;
# print (tempArr[0][0])