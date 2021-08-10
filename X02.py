# Write a Python function that takes a list of words and returns the length of the longest one.
list_of_words = ['Arsham', 'Superman', 'Thor', 'Ironman', 'Artemis']
def longest_word(li):  # li => list
    longest = li[0]
    for word in li:
        if len(word) > len(longest):
            longest = word
    return longest

print(longest_word(list_of_words))
