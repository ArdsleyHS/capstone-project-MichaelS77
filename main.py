def printEquation(items):
  for i in items:
    print(i, end = " ")


def listLength(items):
  length = 0
  for i in items:
    length += 1

#  print("List length = ", length)
  return length - 1

def calculate(number_1,operation,number_2):

  if operation == '*':
    return number_1 * number_2
  elif operation == '+':
    return number_1 + number_2
  elif operation == '/':
    return number_1 / number_2
  elif operation == '-':
    return number_1 - number_2
  else:
    print(f'You entered invalid operation {operation}. Please enter one of: * / + -')
    return 9999999999

def calculator(items):
#  print("length", length)
  answer = 0
  next_answer = 0

  number_1 = items[0]
  i = 1

  while i < listLength(items):
    operation = items[i]
    number_2 = items[i+1]
    
    if operation == '*' or operation == '/':
      answer = calculate(number_1, operation, number_2)
    elif operation == '+' or operation == '-':
      if i+2 >= listLength(items):
        answer = calculate(number_1, operation, number_2)
      # if next operation is of lower priority
      elif items[i+2] == '+' or items[i+2] == '-':
        answer = calculate(number_1, operation, number_2)
      else:
        next_answer = calculate(number_2, items[i+2], items[i+3])
        items[i+1] = next_answer
        items.pop(i+2)
        items.pop(i+2)
        continue
#        print()
#        printEquation(items)
#        print()
    number_1 = answer
    i = i + 2
  
  print(answer) 


operation = "+" 
equation = []

while operation != "=":
  # Getting input 
  number = int(input('Enter number '))
  equation.append(number)

  operation = input('Enter operation or "=" ')
  equation.append(operation)

#print(f'{equation}')

printEquation(equation)
calculator(equation)
