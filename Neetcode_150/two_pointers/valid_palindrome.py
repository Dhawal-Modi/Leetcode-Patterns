class Solution:

    def isPalindrome(self, s: str) -> bool:
        clean_str = ''.join([c.lower() for c in s if c.isalnum()])

        if clean_str == "":
            return True

        i = 0
        j = len(clean_str) - 1
        while i < j:
            if clean_str[i] != clean_str[j]:
                return False
            i += 1
            j -= 1

        return True

if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome("A man%/, a/ plan, a canal: Panama"))
    print(sol.isPalindrome("A man, a plan, a canal: Panama"))
    print(sol.isPalindrome("race a car"))
    print(sol.isPalindrome(" "))