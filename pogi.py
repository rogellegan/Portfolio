"""
Code 1:
a. The output will show this:
J
o
s
e
p
The loop runs 5 times because range(5) produces 0, 1, 2, 3, 4. Each time, name[i] gets the character at that position.
b. There will be an IndexError.
"""
#c.One simple fix is to make the loop stop at the shorter of nChar or the length of the name:
def greet_students(name, nChar):
    for i in range(min(nChar, len(name))):
        print(name[i])

name = input("Enter a Name : ")
nChar = int(input("Enter any numeric number : "))
greet_students(name, nChar)

"""
Code 2:
a. The error is the incorrect indentation of the print() statement and the greet_students() function call. 
I fixed it by properly indenting the print() statement inside the for loop and placing the function call at the correct level.
"""
#b.     

def greet_students(name, nChar): 
    for i in range(nChar, 0, -1): 
        print(name[0:i]) 
name = input("Enter a Name: ") 
greet_students(name, len(name))

"""
Code 3:
a. For example, if n = 3:

1² + 2² + 3² = 14

You can complete the code like this:
"""
def sum_of_squared(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** 2
    return total


n = 0
while n < 1 or n > 100:
    n = input("Enter a Number from 1 to 100 : ")
    n = int(n)

print("Sum of all squared numbers is", sum_of_squared(n))

"""
Explanation:
The `sum_of_squared(n)` function starts with `total = 0`, then loops from `1` to `n`. 
Each number is squared using `i ** 2` and added to `total`. Finally, the function returns the total.
"""