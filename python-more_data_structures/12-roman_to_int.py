#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_dictionary = {"I": 1, "V": 5, "X": 10, "L": 50,
                        "C": 100, "D": 500, "M": 1000}
    total = 0
    prev_value = 0
    for char in reversed(roman_string):
        # Retrieves the value of the Roman numeral,
        # or 0 if the character is invalid
        value = roman_dictionary.get(char, 0)
        # If the current value is lower than the previous one,
        # it is subtracted
        if value < prev_value:
            total -= value
        else:
            total += value
            prev_value = value

    return total
