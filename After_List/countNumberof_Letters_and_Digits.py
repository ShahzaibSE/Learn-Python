sentence = input("Enter Sentence:");
print ("Sentence");
print (sentence.isalpha());

splitSentence = sentence.split(',');
print("Split Sentence")
print(splitSentence)

alphaCounter = 0;
digitCounter = 0;

print("Your Sentence");
for letters in sentence:
    print(letters);
    if(letters.isalpha()):    #Alphabats
        alphaCounter = alphaCounter + 1;
        # print("Alphabet Counter");
        # print (alphaCounter);
    elif (letters.isdigit()):
        digitCounter =  digitCounter + 1;
        # print("Digit Counter");
        # print(digitCounter);
    # else:
        # print("Invalid Data");

# print("Number of letters:"+" "+(alphaCounter))
# print("Number of digit:"+" "+(digitCounter))
print ();
print("Alphabet Counter");
print(alphaCounter);
print("Digit Counter");
print(digitCounter);

testVar = "Batman";
print ("Superhero :"+testVar);