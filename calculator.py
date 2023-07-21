#CALCULATOR
from art import logo
#ADD
def add(n1, n2):
  return n1 + n2


#SUBSTRACT
def substract(n1, n2):
  return n1 - n2

#MULTIPLY
def multiply(n1, n2):
  return n1 * n2

#DIVIDE
def divide(n1, n2):
  if n2 == 0:
    return
  return n1 / n2

operations = {
  "+" : add, "-" : substract, "*" : multiply, "/" : divide,
}
def calculator():
  print(logo)
  num1 = float(input("What's the first number?: "))

  for symbol in operations:
    print(symbol)
  operations_symbol = input("Pick an operation from the line above: ")

  num2 = float(input("What's the second number?: "))

  first_answer = operations[operations_symbol](num1, num2)

  print(f"{num1} {operations_symbol} {num2} = {first_answer}")

  hello = "y"

  while hello: 
    if input("Would you like to continue yes, y, or continue with a new calculation, n?: ") == "y": 
      operations_symbol = input("Pick an operation from the line above: ")
      num3 = float(input("What's the second number?: "))
  
      second_answer = operations[operations_symbol](first_answer, num3)
      print(f"{first_answer} {operations_symbol} {num3} = {second_answer}")
      first_answer = second_answer
    else:
      hello = False
      calculator()

calculator()


