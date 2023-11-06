greeting = input("Greeting: ")
greeting = greeting.strip().lower()

if greeting == "hello" or greeting.split(",", 1)[0] == "hello":
    print("$0")
elif greeting[0] == "h" and greeting != "hello":
    print("$20")
else:
    print("$100")