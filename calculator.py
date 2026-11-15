def add(first_number,second_number):
  return first_number+second_number

def sub(first_number,second_number):
  return first_number-second_number

def mul(first_number,second_number):
  return first_number*second_number

def div(first_number,second_number):
  if second_number==0:
     return "Can't Divide By Zero"
  else : 
     return first_number/second_number
def calculate(first_number,second_number,operator):
  if operator=="+":
    return add(first_number,second_number)
  elif operator=="-":
    return sub(first_number,second_number)
  elif operator=="*":
   return  mul(first_number,second_number)
  elif operator=="/":
   return div(first_number,second_number)
  else:
    return "Invalid Operator"
while True:
  try:
    first_number=float(input("Enter Your First Number: "))
    operator=input("Enter Operator(+,-,*,/): ")
    second_number=float(input("Enter Your Second Number: "))
    print(calculate(first_number,second_number,operator))
  except ValueError:
    print("Invalid Number.Please Enter a Numeric Value.")
    continue
    
  choice=input("Do you want to Continue(Yes/No) :").strip().lower()

  if choice=="no" : 
     break