# Ibrahim Hamdy Mohammed 20231002
# Ahmed Mohammed Ali     20231002
# Anan

counter = 1
number = None

while counter < 2:
    decimal = 0
    print("**numbering system converter**")
    print("A)insert a new number")
    print("B)Exit program")
    input1 = input("Please enter your choice (A/B) ")
    if input1 == 'A':
        number = input("Please insert a number ")
    elif input1 == 'B':
        break
    print("**Please select the base you want to convert a number from**")
    print("2)binary")
    print("10)decimal")
    print("16)hexa decimal")
    print("8)octal")
    base1 = input("enter your base here: ")
    print("**Please select the base you want to convert a number to**")
    print("2)binary")
    print("10)decimal")
    print("16)hexa decimal")
    print("8)octal")
    base2 = input("enter your base here: ")
    if base1 == '2' and base2 == '10' and all(m in "01" for m in number):
        for i in range(len(number)):
            number = number[::-1]
            decimal = decimal + int(number[i])*2**i

    print(decimal)
    print(number)