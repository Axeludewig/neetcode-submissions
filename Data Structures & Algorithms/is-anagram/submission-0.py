class Solution:
    def isAnagram(self, s1: str, s2: str) -> bool:
        # Anagrams must have the same length
        if len(s1) != len(s2):
            return False

        # Store character frequencies from s1
        counts = {}

        for char in s1:
            counts[char] = counts.get(char, 0) + 1

        # Subtract frequencies using s2
        for char in s2:
            # Character does not exist in s1
            if char not in counts:
                return False

            counts[char] -= 1

            # More occurrences in s2 than s1
            if counts[char] < 0:
                return False

        # All character counts matched
        return True