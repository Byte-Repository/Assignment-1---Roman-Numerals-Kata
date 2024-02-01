def arabic_to_roman(number):
    if number == 1:
        return 'I'
    elif number == 2:
        return 'II'
    elif number == 3:
        return 'III'
    elif number == 4:
        return 'IV'
    elif number == 5:
        return 'V'
    elif number == 6:
        return 'VI'
    elif number == 7:
        return 'VII'
    elif number == 8:
        return 'VIII'
    elif number == 9:
        return 'IX'
    elif number == 10:
        return 'X'
    else:
        return ''  # Return an empty string for unsupported numbers

def roman_to_arabic(roman):
    if roman == 'I':
        return 1
    elif roman == 'II':
        return 2
    elif roman == 'III':
        return 3
    elif roman == 'IV':
        return 4
    elif roman == 'V':
        return 5
    elif roman == 'VI':
        return 6
    elif roman == 'VII':
        return 7
    elif roman == 'VIII':
        return 8
    elif roman == 'IX':
        return 9
    elif roman == 'X':
        return 10
    else:
        return 0  # Return 0 for unsupported numerals
