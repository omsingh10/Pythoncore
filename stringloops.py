char = input("enter a String: ")
if len(char) >= 3 and char.endswith("ing"):
  print(char + "ly")
elif len(char) >= 4:
  print(char + "ing")
else:
  print(char)