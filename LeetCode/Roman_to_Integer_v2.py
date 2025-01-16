def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    letters = [char for char in s]
    roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    prev = letters[0]
    for letter in letters:
        if roman_dict[prev] < roman_dict[letter]:
            total -= roman_dict[prev]*2 
        total += roman_dict[letter]
        prev = letter
    return total

print(romanToInt("IX"))