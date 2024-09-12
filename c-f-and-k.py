AllTemps = input("Write one of 3 temp. types (C, F, K): ")
AllTempsUpp = AllTemps.upper()
if AllTempsUpp == "C":
    print("You chose Celsius: C°")
    c = float(input("Now write a temp in Celsius: "))
    print == c
    print("{:.2f}C° converted to F° is {:.2f}F° \nAnd to Kelvin is {:.2f}K°".format(c, c*1.8+32, c+273.15))


elif AllTempsUpp == "F":
    print("You chose Fahrenheit: F°")
    f = float(input("Now write a temp in Fahrenheit: "))
    print == f
    print("{:.2f}F° converted to C° is {:.2f}C° \nAnd to Kelvin is {:.2f}K°".format(f, (f-32)/1.8, (f-32)*5/9+273.15))

elif AllTempsUpp == "K":
    print("You chose Kelvin: K°")
    k = float(input("Now write a temp in Kelvin: "))
    print == k
    print("{:.2f}K° converted to C° is `{:.2f}C° \nAnd to Fahrenheit is {:.2f}F°".format(k, k-273.15, (k-273.15)*9/5+32))

else:
    print("You don't chose a valid temp. type, the program will be closed.")
## Fim do Código ##