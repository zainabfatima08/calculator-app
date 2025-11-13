import math 

def add( a , b):
    return a + b 
def subtract( a , b):
    return a - b 
def multiply( a , b):
    return a * b 
def divide( a , b):
    if b == 0 :
        return "Error!"
    return a / b
def percentage ( a , b) :
    return ( a/ 100 )*b 
def square_root (a):
    if a < 0 :
      return "Error!"
    return math.sqrt(a)

print("Select Operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Percentage")
print("6. Square Root")

while True:
    choice = input("\nEnter choice (1/2/3/4/5/6): ")
    if choice in ('1', '2', '3', '4', '5'):
        num1 = float(input("Enter 1st number: "))
        num2 = float(input("Enter 2nd number: "))

        if choice == '1':
            print("Result : ", add(num1, num2))
        elif choice == '2':
            print("Result : ", subtract(num1, num2))
        elif choice == '3':
            print("Result : ", multiply(num1, num2))
        elif choice == '4':
            print("Result : ", divide(num1, num2))
        elif choice == '5':
            print(f"{num1}% of {num2} is : ", percentage(num1, num2))
    elif choice == '6':
        num = float(input("Enter number to find square root: "))
        print("square root :", square_root(num))
    else:
        print("Invalid Input! Please choose a valid operation ")

    next_calc = input("\nDo you want to calculate again? (yes/no) ").strip()
    if next_calc.lower() != 'yes':
        print("Good Bye!")
        break
