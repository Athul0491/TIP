# Taken captive, Captain Anne Bonny has been smuggled a secret message from her crew. She will know she can trust the message if it contains all of the letters in the alphabet. Given a string message containing only lowercase English letters and whitespace, write a function can_trust_message() that returns True if the message contains every letter of the English alphabet at least once, and False otherwise.


def can_trust_message(message):
    if len(message) < 26:
        return False
    boss = set()
    for i in message:
        if i != " ":
            boss.add(i)
    return len(boss) == 26


# Example Usage:

message1 = "sphinx of black quartz judge my vow"
message2 = "trust me"

print(can_trust_message(message1))
print(can_trust_message(message2))
# Example Output:

# True
# False
