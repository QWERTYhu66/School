g = int(input())

if g < 250:
  print("FLYWEIGHT")
elif g >= 250 and g < 900:
  print("LIGHTWEIGHT")
elif g >= 900 and g < 4000:
  print("MIDDLEWEIGHT")
else:
  print("HEAVYWEIGHT")