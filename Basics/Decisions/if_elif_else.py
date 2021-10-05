#User input
print("Towards which direction should I paint(up, down, left or right)?")
painting_type = input()

#direction of painting
if painting_type == "up":
    print("I am painting in an upward direction")

elif painting_type == "down":
    print("I am painting in a downwards direction")

elif painting_type == "left":
    print("I am painting in a leftward direction")

elif painting_type == "right":
    print("I am painting in a rightward direction")

else:
    print("I dont know which way to paint")

print("painting completed!")