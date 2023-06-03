import time as t

with open("test.txt") as f:
    data = f.readlines()
    for line in data:
        print(line, end="")

with open("test.txt", "w") as f:
    f.write("New line is added!!!\n")
    f.write("I changed all the lines to this")


"""
Ask the user if they want to add anything to the file.
If they want to add things to the file, add a new 
user input text to the file.
"""

print("Welcome to the file manager!")
add_or_no = input("Do you want to add content to the file?(y/n)\n").lower()
if add_or_no == "n":
    print("Goodbye!")
elif add_or_no == "y":
    print("Now accessing file")
    t.sleep(1)
    print("...")
    t.sleep(1)
    with open("test.txt", "a") as f:
        f.write("\n"+input('what do you want to add?\n'))
else:
    print("You didn't put a readable command. Goodbye!")

"""
read from the .csv
examine the incomes of each entry
print out the name of the person with the largest income
"""
with open("data.csv", "r") as data:
    max_income = 0
    max_earner = ""
    for line in data.readlines():
        entry = line.split()
        try:
            if max_income < int(entry[2]):
                max_income = int(entry[2])
                max_earner = entry[0]
        except:
            pass
    print(max_income, max_earner)
