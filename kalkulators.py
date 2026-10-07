num1 = float(input("Ievadi pirmo skaitli: "))
op = input("Ievadi darbību (+, -, *, /): ")
num2 = float(input("Ievadi otro skaitli: "))

if op == "+":
    print(num1 + num2)

elif op == "-":
    print(num1 - num2)

elif op == "*":
    print(num1 * num2)

elif op == "/":
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Ar 0 dalīt nedrīkst!")

else:
    print("Nepareiza darbība!")