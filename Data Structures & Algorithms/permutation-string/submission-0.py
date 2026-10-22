class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        s1_count = [0] * 26
        s2_count = [0] * 26
        
        # Populate frequency counts for s1 and the first window of s2
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1
            
        matches = 0
        for i in range(26):
            if s1_count[i] == s2_count[i]:
                matches += 1
                
        # Slide the window over s2
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
                
            # Add the new character entering the window on the right
            right_char = ord(s2[r]) - ord('a')
            s2_count[right_char] += 1
            if s2_count[right_char] == s1_count[right_char]:
                matches += 1
            elif s2_count[right_char] == s1_count[right_char] + 1:
                matches -= 1
                
            # Remove the old character leaving the window on the left
            left_char = ord(s2[l]) - ord('a')
            s2_count[left_char] -= 1
            if s2_count[left_char] == s1_count[left_char]:
                matches += 1
            elif s2_count[left_char] == s1_count[left_char] - 1:
                matches -= 1
                
            l += 1
            
        return matches == 26