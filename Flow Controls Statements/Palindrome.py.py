value=input("Enter any value: ")
if(value.upper()==value[::-1].upper()):
    print("{} is a Palindrome".format(value))
if(value.upper()!=value[::-1].upper()):
    print("{} is not a Palindrome".format(value))
print("Program executed Succesfully")