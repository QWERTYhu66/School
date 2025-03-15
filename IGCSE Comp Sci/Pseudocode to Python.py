# Question 1
Answer = int(input())
Correct = False if Answer < 0 or Answer > 100 else True

# Question 2
Binary = ""
Denary = int(input("Enter a denary number: "))

while Denary != 0:
    Binary = str(Denary % 2) + Binary
    Denary //= 2

print(Binary)

# Question 3
Base = float(input("What number do you want to see the powers of? "))
Powers = [Base ** i for i in range(1, 11)]

print(Powers)

# Question 4
def Line(Size: int):
    print('-' * Size)

def DefaultLine():
    Line(60)

DefaultLine()

# Question 5
def Pythagoras(N1: int, N2: int) -> float:
    return (N1**2 + N2**2) ** 0.5

A = int(input("Enter first number: "))
B = int(input("Enter second number: "))

Result = Pythagoras(A, B)

print("Hypotenuse Length:", Result)

# Question 6
Move = input("Enter move (W/A/S/D): ").upper()
Position = 0

match Move:
    case 'W':
        Position -= 10
    case 'S':
        Position += 10
    case 'A':
        Position -= 1
    case 'D':
        Position += 1
    case _:
        print("Beep")

# Question 7
ChallengerName = input("Enter Challenger's name: ")
ChampionName = input("Enter Champion's name: ")
Player1Name = ChallengerName
ChallengerScore = int(input("Enter Challenger's score: "))
ChampionScore = int(input("Enter Champion's score: "))
HighestScore = int(input("Enter Highest score: "))

if ChallengerScore > ChampionScore:
    if ChallengerScore > HighestScore:
        print(ChallengerName, "is champion and highest scorer")
    else:
        print(Player1Name, "is the new champion")
else:
    print(ChampionName, "is still the champion")
    if ChampionScore > HighestScore:
        print(ChampionName, "is also the highest scorer")

# Question 8
Password = ""

while Password != "Secret":
    Password = input("Please enter the password: ")

# Question 9
Word = "What is this?"

Found = False
Position = 0

while not Found:
    Letter = Word[Position].upper()
    if Letter == 'I':
        Found = True
    Position += 1