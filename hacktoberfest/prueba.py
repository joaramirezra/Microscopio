opciones = ["Simple Calculator","1.Add","2.Substract","3.Multiply","4.Divide",
             "5.Square","6.Power","7.Square Root","8.Odd/Even","9.Check if Prime"
            ,"10.Quit"]

[print(valor) for valor in opciones ]

def Read_two_Values():
    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))
    return number1,number2

while True:
    option = int(input("Enter a number to excute operation:  "))
    if option == 10:
        break
    elif option == 1:
        number1,number2 = Read_two_Values()
        print(number1 + number2)
    elif option == 2:
        number1,number2 = Read_two_Values()
        print(number1 - number2)
    elif option == 3:
        number1,number2 = Read_two_Values()
        print(number1 * number2)
    elif option == 4:
        number1,number2 = Read_two_Values()
        print(number1 / number2)
    elif option == 5:
        number1 = float(input("Enter a number: "))
        print(number1**2)
    elif option == 6:
        number1 = float(input("Enter the number to find its value: "))
        number2 = float(input("Enter a value of power: "))
        print(number1 ** number2)
    elif option == 7:
        number1 = float(input("Enter a number: "))
        print(number1 ** 0.5)
    elif option == 8:
        number1 = float(input("Enter a number: "))
        if number1%2==0:
            print("Even")
        else:
            print("Odd")
    elif option == 9:
        def prime_no(n) :
            if (n <= 1 or n <= 3 ) :
                return False
            if (n % 2 == 0 or n % 3 == 0) :
                return False
            temp = 5
            while(temp * temp <= n) :
                if (n % temp == 0 or n % (temp + 2) == 0) :
                    return False
                temp = temp + 6

            return True
        number = int(input("Enter a number to check if it is a prime no: "))
        print("You entered {}.".format(number))

        if prime_no(number):
            print("And the number {} is a Prime Number".format(number))
        else:
            print("And the number {} is not a Prime Number.".format(number))


    else :
        print("Invalid Input")
print("EXIT")

