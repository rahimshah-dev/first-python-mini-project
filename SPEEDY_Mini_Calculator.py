#WELCOME TO MY MINI CALCULATOR SPEEDY :)

''' The main function will allow me to enable
    the program understand other integrated functions
    before give the required value. '''
def main():
  #   Keep the calculations going for the user without
  #   needing to run the program over and over again.
  while True:
    print("\n\nWelcome to SPEEDY Calculator!\nFollow along to do your calculation smoothly:")
    #   Error handling in case the user inputs a string or other datatype.
    try:
      #   Choosing the operation.
      op = int(input("Please provide the number of the operation you want to proceed with,\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Others\n6. Exit\nOperation: "))
      if 0 < op < 6:
        #   Values to operate on.
        a = int(input("Value a: "))
        b = int(input("Value b: "))
        #   Op is the value for the operation so with match and case,
        #   the program can proceed with the relative operation.
        match op:
          case 1:
            print(a+b)
          case 2:
              print(a-b)
          case 3:
              print(a*b)
          case 4:
              #   Handling division error.
              try:
                print(a/b)
              except ZeroDivisionError:
                print("Zero Division Error!")
          case _:
            break
      #   If the operation user wants isn't available.
      else:
        print(f"Apologies! Currently the system does not support operation {op} at the moment.")
    #   In case of value error.
    except:
      print("That's not the correct input!\nTry again...")
    

main()