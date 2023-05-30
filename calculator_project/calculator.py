from calculator_art import calculator
#Calculator Functions
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2): 
  return n1 * n2
  
def divide(n1, n2): 
  return n1 / n2

#Dictionary
operations = {
"+": add,
"-": subtract,
"*": multiply,
"/": divide
}

#Main Function
def calculator():
  continue_calculation = "y"
  answer = ""
  while continue_calculation == 'y':
    if answer == "":
      num1 = int(input("What's the first number?: "))
    else:
      num1 = answer
    
    for symbol in operations:
      print(symbol)
    
    operation_symbol = input("Pick an operation from the lines above: ")
    num2 = int(input("What's the next number?: "))
    answer = operations[operation_symbol](num1, num2)
    
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    
    continue_calculation = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to perform a new calculation.: ")
    
    if continue_calculation == "n":
      calculator()
      
#Start of Script
print(calculator)
calculator() 


 
  
    
    
    
  
  


