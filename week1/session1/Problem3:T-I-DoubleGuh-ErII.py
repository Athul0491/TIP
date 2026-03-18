# T-I-Double Guh-Er: That spells Tigger! Write a function tiggerfy() that accepts a string word and returns a new string that removes any substrings t, i, gg, and er from word. The function should be case insensitive.


def tiggerfy(word):
    to_remove = ["t", "i", "gg", "er"]
    for i in to_remove:
        word = word.replace(i.lower(), "")
        word = word.replace(i.upper(), "")
    return word


word = "Trigger"
print(tiggerfy(word))

word = "eggplant"
print(tiggerfy(word))

word = "Choir"
print(tiggerfy(word))

# "r"
# "eplan"
# "Chor"
