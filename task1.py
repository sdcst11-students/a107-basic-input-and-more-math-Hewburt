'''
##### Task 1 Percent Error
Ask the user to input the following:
* the expected number
* the actual result
Calculate the percent difference between the two results. Round your answer to 2 decimal places

```
https://www.skillsyouneed.com/num/percent-change.html

Sample Output:
Enter expected: 10
Enter actual : 9
The percent difference is -10.0%

Enter expected: 12
Enter actual : 14
The percent difference is 16.67%
```
'''
expected = float(input("Enter expected: "))
actual = float(input("Enter actual: "))

percent_difference = ((actual - expected) / abs(expected)) * 100

percent_difference = round(percent_difference, 2)

print(f"The percent difference is {percent_difference}%")