#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return (0)
    if roman_string is None:
        return (0)
    dc = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    decim = 0

    for i in range(len(roman_string)):
        if dc.get(roman_string[i], 0) == 0:
            return (0)

        if (i != (len(roman_string) - 1) and
                dc[roman_string[i]] < dc[roman_string[i + 1]]):
                decim += dc[roman_string[i]] * -1

        else:
            decim += dc[roman_string[i]]
    return (decim)
