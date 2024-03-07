# Ibrahim Hamdy Mohammed 20231002
# Ahmed Mohammed Ali     20230033
# Anan Hamdi Ali         20231117

counter = 1
number = None
while counter < 2:     # an infinite while loop stops when user enters B so the programme is working till user close it
    decimal = 0
    print("**numbering system converter**\n"+"A)insert a new number\n"+"B)Exit program")
    input1 = input("Please enter your choice (A/B) ").upper()
    if input1 == 'A':
        number = input("Please insert a number: ")
    elif input1 == 'B':
        print("Exited program")
        break
    else:
        print("Error:enter either A or B"+"\n")
        continue
    print("**Please select the base you want to convert a number from**")
    print("2)binary\n"+"10)decimal\n"+"16)hexa decimal\n"+"8)octal")

    base1 = input("enter your base here: ")
    if base1 == '10' and not all(char in "0123456789"for char in str(number)):  # to validate user input with the base
        print(f'Error:{number} is not valid in base 10 ')
        continue
    if base1 == '2' and not all(char in "01" for char in str(number)):
        print(f'Error:{number} is not valid in base 2 ')
        continue
    if base1 == '8' and not all(char in "01234567"for char in str(number)):
        print(f'Error:{number} is not valid in base 8 ')
        continue
    if base1 == '16' and not all(char in "0123456789ABCDEF"for char in str(number).upper()):
        print(f'Error:{number} is not valid in base 16 ')
        continue
    if base1 not in ['2', '16', '8', '10']:
        print("Error:select a valid choice")
        continue
    print("**Please select the base you want to convert a number to**")
    print("2)binary\n" + "10)decimal\n" + "16)hexa decimal\n" + "8)octal")
    base2 = input("enter your base here: ")
    if base2 not in ['2', '16', '8', '10']:
        print("Error:select a valid choice")
        continue

    def all_to_decimal(input_number):           # a function that converts from binary,octal,hexadecimal to decimal
        arr = [x for x in reversed(input_number.upper())]  # to list the input in a reversed order

        for i in range(len(arr)):       # a for loop to check A,B,C,D,E,F and assign the corresponding values if existed
            if arr[i] == 'A':
                arr[i] = 10             # binary 100 to decimal 4
            elif arr[i] == 'B':         # octal 12   to decimal 10
                arr[i] = 11             # hexadecimal 1AB to decimal
            elif arr[i] == 'C':
                arr[i] = 12
            elif arr[i] == 'D':
                arr[i] = 13
            elif arr[i] == 'E':
                arr[i] = 14
            elif arr[i] == 'F':
                arr[i] = 15
        result = 0

        for i, n in enumerate(arr):   # using enumerate function i as the index and n the actual numbers of the list
            result += int(base1) ** int(i) * int(n)  # multiplying the base raised to the power of the index by the num

        return result

    func1 = all_to_decimal(number)
    if (base1 == '2' and base2 == '10' and all(char in "01" for char in str(number))) or \
       (base1 == '8' and base2 == '10' and all(char in "01234567" for char in str(number))) or \
       (base1 == '16' and base2 == '10' and all(char in "0123456789ABCDEF" for char in str(number).upper())):
        print(func1)    # conditions if  any of them is met the function get the recall and convert from 3systems to dec

    def decimal_to_all(input_number):  # defining a function converts from decimal to any of the other3 numbering system
        arr = []
        while input_number >= int(base2):  # while loop works as long as the number or the quotient is greater than base
            arr.append(input_number % int(base2))    # to add the remainder to  the list
            input_number = input_number // int(base2)  # setting the last value for input number (quotient) later
        if input_number < int(base2):   # if the quotient is less than the base (divisor) append it as it is
            arr.append(input_number)
        for i in range(len(arr)):  # a for loop to check A,B,C,D,E,F and assign the corresponding values if existed
            if arr[i] == 10:
                arr[i] = 'A'     # decimal 4  to binary 100
            elif arr[i] == 11:   # decimal 10 to octal 12
                arr[i] = 'B'     # hexadecimal 1AB to decimal 427
            elif arr[i] == 12:
                arr[i] = 'C'
            elif arr[i] == 13:
                arr[i] = 'D'
            elif arr[i] == 14:
                arr[i] = 'E'
            elif arr[i] == 15:
                arr[i] = 'F'
        arr.reverse()
        for char in arr:
            print(char, end='')  # to get the numbers out of the list and line them up
        print()                  # empty line

    if (base1 == '10' and base2 == '2' and int(number) >= 0) or \
       (base1 == '10' and base2 == '8' and int(number) > 0) or \
       (base1 == '10' and base2 == '16' and int(number) > 0):  # conditions if met any conversion to dec happens
        decimal_to_all(int(number))          # the recall of the function if any condition is met

    def binary_to_octal(input_number):   # a function to convert from binary to octal
        func = all_to_decimal(input_number)
        decimal_to_all(func)

    if base1 == '2' and base2 == '8' and all(char in "01" for char in str(number)):
        binary_to_octal(number)

    def octal_to_binary(input_number):   # a function to convert from octal to binary
        func = all_to_decimal(input_number)
        decimal_to_all(func)

    if base1 == '8' and base2 == '2' and all(char in "01234567" for char in str(number)):
        octal_to_binary(number)

    def binary_to_hexadecimal(input_number):  # a function to convert from binary to hexadecimal
        func = all_to_decimal(input_number)
        decimal_to_all(func)
    if base1 == '2' and base2 == '16' and all(char in "01" for char in str(number)):
        binary_to_hexadecimal(number)

    def hexadecimal_to_binary(input_number):  # a function to convert from hexadecimal to binary
        func = all_to_decimal(input_number)
        decimal_to_all(func)
    if base1 == '16' and base2 == '2' and all(char in '0123456789ABCDEF' for char in str(number).upper()):
        hexadecimal_to_binary(number)

    def hexadecimal_to_octal(input_number):   # a function to convert from hexadecimal to octal
        func = all_to_decimal(input_number)
        decimal_to_all(func)
    if base1 == '16' and base2 == '8' and all(char in '0123456789ABCDEF' for char in str(number).upper()):
        hexadecimal_to_octal(number)

    def octal_to_hexadecimal(input_number):  # a function to convert from octal to hexadecimal
        func = all_to_decimal(input_number)
        decimal_to_all(func)
    if base1 == '8' and base2 == '16' and all(char in "01234567" for char in str(number)):
        octal_to_hexadecimal(number)
                                    #****** Test ******
    # def all_to_decimal(100) base1 ==2 ,result 4
    # def all_to_decimal(12) base1 ==8 ,result 10
    # def all_to_decimal(1A) base1 == 16 ,result 26
    # def decimal_to_all(26) base2 == 16 ,result 1A
    # def decimal_to_all(10) base2 == 8 ,result 12
    # def decimal_to_all(4) base2 == 2 ,result 100
    # def binary_to_octal(1010) ,result 12
    # def octal_to_binary(12) ,result 1010
    # def binary_to_hexadecimal(11010) ,result 1A
    # def hexadecimal_to_binary(1A) ,result 11010
    # def hexadecimal_to_octal(1A) ,result 32
    # def octal_to_hexadecimal(32) ,result 1A
