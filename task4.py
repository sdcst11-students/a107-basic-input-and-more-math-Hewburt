#!python3

"""
Write a program to ask the user to input a length in centimeters. Convert this into feet and inches.  Round your inches to the nearest whole inch.
You will likely need to make use of at least one of the following:
* % modulus
* math.floor()

Sample output:
```
Enter a length in centimeters: 172
172 centimeters is 5 feet and 8 inches

Enter a length in centimeters: 32
32 centimeters is 1 feet and 1 inches
```
"""

centimeters = int(input("Enter a length in centimeters: "))

inches = centimeters / 2.54  # 1 inch is 2.54 centimeters
feet = int(inches // 12)  # Get the whole number of feet
remaining_inches = round(inches % 12)  # Get the remaining inches and round to the nearest whole inch

print(f"{centimeters} centimeters is {feet} feet and {remaining_inches} inches")