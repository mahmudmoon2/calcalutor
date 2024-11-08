print("Welcome to calculator project")
print("1. Addition")
print("2. Substraction")
print("3. Multiply")
print("4. Division")

option = int(input("Select an option for basic calculator Operation: "))

if option == 1:
    n1 = int(input("Enter 1st number: "))
    n2 = int(input("Enter 2nd number: "))
    n3 = n1 + n2
    print("Addition is " + str(n3))
elif option == 2:
    n1 = int(input("Enter 1st number: "))
    n2 = int(input("Enter 2nd number: "))
    n3 = n1 - n2
    print("Substraction is " + str(n3))
elif option == 3:
    n1 = int(input("Enter 1st number: "))
    n2 = int(input("Enter 2nd number: "))
    n3 = n1 * n2
    print("Multiply is " + str(n3))
elif option == 4:
    n1 = int(input("Enter 1st number: "))
    n2 = int(input("Enter 2nd number: "))
    n3 = n1 / n2
    print("Division is " + str(n3))
else:
    print("invalid input")