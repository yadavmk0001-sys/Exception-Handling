try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    result = num1/num2
    print("Result is : ", result)

except ZeroDivisionError:
    print("It is not allowed")
except ValueError:
    print("Enter numbers")
except:
    print("Some error")
finally:
    print("I will execute no matter what happens")