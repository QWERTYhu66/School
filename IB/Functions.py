def say_goodbye(name: str):
    print(f"Goodbye, {name}!")

def excited_greet(name: str):
    name = name.upper();
    print(f"HELLO {name}!!!")

def takeTwoNames(name1: str, name2: str):
    print(f"Hello {name1} and {name2}!")

say_goodbye(input("Enter a name: "))
excited_greet(input("Enter a name: "))
takeTwoNames(input("Enter the first name: "), input("Enter the second name: "))