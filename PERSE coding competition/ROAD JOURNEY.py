r1 = input()

if r1 == "M43":
  r2 = input()
  if r2 == "A31":
    print("zoo")
  elif r2 == "A17":
    print("cinema")
  elif r2 == "A59":
    r3 = input()
    if r3 == "B1031":
      print("park")
    elif r3 == "B598":
      print("campsite")
else:
  print("unknown")