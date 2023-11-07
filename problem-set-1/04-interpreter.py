expresion =  input("Expresion: ")

x, y, z = expresion.split(" ")
x = float(x)
z = float(z)

match y:
    case "+":
        print(x + z)
    case "-":
        print(x - z)
    case "*":
        print(x * z)
    case "/":
        print(x / z)
    case _:
        print("Try again please")


#print(expresion)
#print(x - z)

#x, y, z = expression.split(" ")
