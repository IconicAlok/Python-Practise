# exception = an event that interrupts the flow of the program
#            (ZeroDivisionError, TypeError, ValueError)
#            1. try, 2. except, 3. finnally

try:
    number = int(input("Enter a number: "))
    print(1/number)
except ZeroDivisionError:
    print("You can't divided by zero IDIOT!")
except ValueError:
    print("Enter only number please!")
except Exception:
    print("Someting went wrong!")
finally:
    print("Do something clean up here!")