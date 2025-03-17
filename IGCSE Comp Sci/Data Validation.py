while True:
    p = input("Enter password: ")
    if any(c.isupper() for c in p) and any(c.islower() for c in p) and any(c.isdigit() for c in p) and any(c in '@$!%*?&' for c in p) and len(p) >= 8:
        break
    print("Invalid password! Must be at least 8 characters long, include uppercase, lowercase, a number, and a special character (@$!%*?&). Try again.")

while True:
    a = input("Enter age: ")
    if a.isdigit() and 0 <= int(a) <= 130:
        break
    print("Invalid age! Try again.")

while True:
    i = input("Enter ARC/ID: ")
    if len(i) == 10 and i[0].isalpha() and i[0].isupper() and i[1:].isdigit():
        break
    print("Invalid ARC/ID format! The first character must be an uppercase letter (A-Z), followed by nine digits (e.g., A123456789). Try again.")

while True:
    d = input("Enter date (YYYY-MM-DD): ")
    if d.count('-') == 2 and all(x.isdigit() for x in d.split('-')) and 1 <= int(d.split('-')[1]) <= 12 and 1 <= int(d.split('-')[2]) <= 31:
        break
    print("Invalid date format! Try again.")