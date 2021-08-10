# Get all possible two digit letter combinations from a digit string
# way 1:
string_maps = {
                "1": "abc",
                "2": "def",
                "3": "ghi",
                "4": "jkl",
                "5": "mno",
                "6": "pqrs",
                "7": "tuv",
                "8": "wxy",
                "9": "z"
            }
upper_bound = len(string_maps) + 1
for i in range(1, upper_bound):
    for j in range(1, upper_bound):
        if i == j:
            break
        for letter_i in string_maps[f'{i}']:
            for letter_j in string_maps[f'{j}']:
                print(f'{letter_j}{letter_i}')
