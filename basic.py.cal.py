print('press 1. to add')
print('press 2. to subtract')
print('press 3. to divide')
print('press 4. to multiply')
print()
operation = input()

if operation == '1':
  num1 = eval(input('Enter the first number you want to add '))
  num2 = eval(input('Enter the second number you want to add '))
  print('the answer is', num1 + num2 ,)
print()
if operation == '2':
  num1 = eval(input('Enter the first number you want to subtract '))
  num2 = eval(input('Enter the second number you want to subtract '))
  print('the answer is', num1 - num2 ,)
print()
if operation == '3':
  num1 = eval(input('Enter the first number you want to divide '))
  num2 = eval(input('Enter the second number you want to divide '))
  print('the answer is', num1 // num2 ,)
print()
if operation == '4':
  num1 = eval(input('Enter the first number you want to multiply '))
  num2 = eval(input('Enter the second number you want to multiply '))
  print('the answer is', num1 * num2 ,)
print()