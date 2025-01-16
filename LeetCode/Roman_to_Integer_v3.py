class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        tab = {"": 0, "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        "If just one letter, return its value"
        "Otherwise, return the value of the first letter, multiplied by -1 if it is smaller than the second letter, plus the value of the rest of the string - recursive call"
        return tab[s] if len(s) <= 1 else tab[s[0]] * (-1 if tab[s[0]] < tab[s[1]] else 1) + self.romanToInt(s[1:])
    
def main():
    solution = Solution()
    test_cases = ["IX", "III", "LVIII", "MCMXCIV"]
    for case in test_cases:
        print(f"{case}: {solution.romanToInt(case)}")

if __name__ == "__main__":
    main()