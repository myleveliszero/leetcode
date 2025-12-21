from string import ascii_lowercase, ascii_uppercase
class Solution:
    def isPalindrome(self, s: str) -> bool:
        hmap_up = {up:low for low, up in zip(ascii_lowercase, ascii_uppercase)}
        new_str = []
        for char in s:
            if char in hmap_up:
                new_str.append(hmap_up[char])
            if 97 <= ord(char) <= 122 or 48<= ord(char) <= 57:
                new_str.append(char)
        new_str = "".join(new_str)
        left, right = 0, len(new_str)-1
        while left < right:
            if new_str[left] != new_str[right]:
                return False
            left += 1
            right -= 1
        return True


print(Solution().isPalindrome(s = "A man, a plan, a canal: Panama"))
        