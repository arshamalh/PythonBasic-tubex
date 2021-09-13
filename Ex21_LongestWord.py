# Check out my Youtube channel:
# https://www.youtube.com/channel/UCRYxPJle46XMws4ewJE-ShQ

# Write a Python function that takes a list of words and returns the length of the longest one.
def longest_word(li):  # li => list
    longest = li[0]
    for word in li:
        if len(word) > len(longest):
            longest = word
    return longest

list_of_words = ['Arsham', 'Superman', 'Thor', 'Ironman', 'Artemis']
print(longest_word(list_of_words))
