class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        tab = {"": 0, "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        return tab[s] if len(s) <= 1 else tab[s[0]] * (-1 if tab[s[0]] < tab[s[1]] else 1) + self.romanToInt(s[1:])
    
print(Solution().romanToInt("IX"))

# Example usage
solution = Solution()
test_cases = ["IX", "III", "LVIII", "MCMXCIV", "CDXLIV"]
for case in test_cases:
    print(f"{case}: {solution.romanToInt(case)}")