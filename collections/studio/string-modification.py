my_string = "LaunchCode"


# a) Use string methods to remove the first three characters from the string and add them to the end.
new_string = my_string[3:] +  my_string [:3]
print(new_string)


# Use a template literal to print the original and modified string in a descriptive phrase.
print (f"The original string was {my_string} and the modified string is {new_string}.")


# b) Modify your code to accept user input. Query the user to enter the number of letters that will be relocated.
question = int(input('How many digits should be relocated?'))

new_string = my_string[question:] +  my_string [:question]



# c) Add validation to your code to deal with user inputs that are longer than the word. In such cases, default to moving 3 characters. Also, the template literal should note the error.
if question > len(my_string):
    print ("Please print a number between 0 and 9")