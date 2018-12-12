a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

#Getting matching elements of lists
temp_list = [];
counter = 0;

for val_list_a in a:
    for val_list_b in b:

        if val_list_a == val_list_b:
            print("Matched element:"+" "+str(val_list_a));
            temp_list.append(val_list_a);

print("Temporary list:"+" "+str(temp_list));


print("Counter");
print(counter);

final_result = set(temp_list);   #Here set function removes duplicates from list.
print("Final list:"+" "+str(final_result));
