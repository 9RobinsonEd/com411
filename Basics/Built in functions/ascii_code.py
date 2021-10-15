#built in functions

print("Program Started")
print("")

print("Please enter a standard character:")
character = input()

if len(character) == 1:
    print(f"The ACII code for {character} is {ord(character)}")
else:
    print("This is not a suitable character")

print("program ended")