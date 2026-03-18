# Tigger has developed a new programming language Tiger with only four operations and one variable tigger.

# bouncy and flouncy both increment the value of the variable tigger by 1.
# trouncy and pouncy both decrement the value of the variable tigger by 1.
# Initially, the value of tigger is 1 because he's the only tigger around! Given a list of strings operations containing a list of operations, return the final value of tigger after performing all the operations.


def final_value_after_operations(operations):
    trigger = 1
    for i in operations:
        if i == "bouncy" or i == "flouncy":
            trigger += 1
        if i == "trouncy" or i == "pouncy":
            trigger -= 1
    return trigger


operations = ["trouncy", "flouncy", "flouncy"]
final_value_after_operations(operations)
# 2

operations = ["bouncy", "bouncy", "flouncy"]
final_value_after_operations(operations)
# 4
