valid = False
while not valid:
    try:
        n = int(input("Enter a number: "))
        if n % 2 == 0:
            print("bye")
            valid = True
        else: print("It is not even")
    except ValueError:
        print("Please write numerical value")