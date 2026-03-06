a = int(input("Enter your number: "))
b = int(input("Enter your number: "))

print("Kiya karna hai?")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divide (/)")

choice = int(input("Apna choice dalo (1/2/3/4): "))

if choice == 1:
    result = a + b
    print("Addition =", result)

elif choice == 2:
    result = a - b
    print("Subtraction =", result)

elif choice == 3:
    result = a * b
    print("Multiplication =", result)

elif choice == 4:
    if b != 0:
        result = a / b
        print("Division =", result)
    else:
        print("Zero se divide nahi hota!")

else:
    print("Invalid choice!")