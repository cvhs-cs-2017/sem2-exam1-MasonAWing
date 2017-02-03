"""Use the range function to print the numbers from 40 to 1 (backwards)"""

for x in range(1, 41):
    while x > 0:
        print(x)
        x = x - 1

"""Repeat the exercise but count by 5's"""
for x in range(1, 41):
    while x > 0:
        print(x)
        x = x - 5


"""Write a program that will count print first 10 the multiples of (n) where n is
taken from user input.  Include necessary print statements."""
print('may i take your number')
n = int(input())
def multiples(n, count):
    for x in range(0, count*n, n):
        print(x)
multiples(n, 10)
