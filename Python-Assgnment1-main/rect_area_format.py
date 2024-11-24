# Prompting user for the rectangle's dimensions
length = float(input('Enter the length of the rectangle: '))
width = float(input('Enter the width of the rectangle: '))

# Calculating the area
area = length * width

# Displaying the area with two decimal places using format method
print("Area of the rectangle: {:.2f}".format(area))
