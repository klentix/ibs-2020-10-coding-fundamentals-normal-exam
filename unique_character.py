# Unique Characters
# Create a function that takes a string as parameter
# and returns a list with the unique letters of the given string.
#
# Write 2 different unit test cases for the method.
#
# Example
# Input
#
# "anagram"
# Output
#
# ["n", "g", "r", "m"]
# #
# #
import sys

def unique_character(word):

    word_frequency = []
    duplicate =[]
    for i in word:
        if i not in word_frequency:
            word_frequency.append(i)
        else:
            duplicate.append(i)
    return (set(word_frequency) - set(duplicate))





print(unique_character("anagram"))
print(unique_character("like"))

