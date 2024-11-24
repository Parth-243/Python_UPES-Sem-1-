#Taking user input for first & last name
f_name = input('Enter your first name : ')
l_name = input('Enter your last name : ')

#using string slicing to reverse the name [the script used string slicing to reverse the strings & concatenation to join them with a space]

rev_name = l_name[::-1] + ' ' + f_name[::-1]

#printing the reversed name

print('Reversed Name:', rev_name)
