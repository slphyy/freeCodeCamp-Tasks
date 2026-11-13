def change_string(string):
    if string == "":
        return ""
    print(f'{string[0]}')
    return change_string(string[1:]) + string[0]

print(change_string('monokono'))