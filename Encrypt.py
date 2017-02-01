"""Write a code that will remove vowels from a string and run it for the sentence:

'Computer Science Makes the World go round but it doesn't make the world round itself!'

Print the save the result as the variable = NoVowels
"""
import random
def novowels(s):
    vowels = "aeiouAEIOU"
    word = ""
    for x in s:
        if x in vowels:
            x = ""
        word += x
    return word
print(novowels('Computer Science Makes the World go round but it doesn\'t make the world round itself!'))

"""Write an encryption code that you make up and run it for the variable NoVowels"""
def chaos(s):
    consonants = "bcdfghjklmnpqrstvxzBCDFGHJKLMNPQRSTVXZ"
    word = ""
    for x in s:
        for x in s:
            if x in consonants:
                x = random.randint(1, 6)
                if x == 1:
                    x = "$"
                if x == 2:
                    x = "#"
                if x == 3:
                    x = "%"
                if x == 4:
                    x = "^"
                if x == 5:
                    x = "&"
                if x == 6:
                    x = "*"
        word += x
    return word
print(chaos(novowels('Computer Science Makes the World go round but it doesn\'t make the world round itself')))
