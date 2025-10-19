try :
    num=int(input("Enter the value: "))
    print(num)
except ValueError as ex:
    print("Exception:", ex)
print("I am outside the try block")