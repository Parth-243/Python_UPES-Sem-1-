#imput()= A function that prompts the user to enter data
#         Returns the entered data as a string

#Creating an shopping card
print("Name of Products:-")
print('1.Shirt')
print('2.T-Shirt')
print('3.Jence')
print('4.trouser ')
item= input('Enter the name of Product: ')
# typecasting the str into int
quantity= int(input('Enter the total quantity: ')); 

if("Shirt"==item):
  price=400
  total_price= 400*quantity
elif("T-Shirt"==item):
  price=200
  total_price= 200*quantity
elif("Jence"==item):
  price=1000
  total_price= 1000*quantity
elif("Trouser"==item):
  price=500
  total_price= 500*quantity
else:
  print("Sorry we dont have the Product")
print('\n')
print(f'You have Purchase: {item}')
print(f'Price: {price}')
print(f'The Total no. of Quantity: {quantity}')
print(f'The Total Price: {total_price}')



