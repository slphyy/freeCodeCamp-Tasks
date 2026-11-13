def verify_card_number(number):
    digits = [int(char) for char in number if char.isdigit()]

    digits.reverse()

    total = 0
    for index, digit in enumerate(digits):
        if index % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit

    if total % 10 == 0:
        return 'VALID!'
    return 'INVALID!'

print(verify_card_number('453914889'))