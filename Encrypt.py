"""Write a code that will remove vowels from a string and run it for the sentence:

'Computer Science Makes the World go round but it doesn't make the world round itself!'

Print the save the result as the variable = NoVowels
"""
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
