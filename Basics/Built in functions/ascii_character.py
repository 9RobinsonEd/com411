#Converting back to ascii

print("Program Started")
print("")
print("Please enter an ASCII code:")
code = int(input())

if code >=32 and code <= 126:
    print(f"The character represented by ASCII code{code} is {chr(code)}")
else:
    print("This is not a valid number")
print("Program ended!")
