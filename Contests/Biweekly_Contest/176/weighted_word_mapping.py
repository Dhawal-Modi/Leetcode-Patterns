from typing import List

class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]):
        result_str = []
        for word in words:
            word_sum = 0
            for char in word:
                word_sum += weights[ord(char) - ord('a')]
            result = chr(ord('z') - (word_sum % 26))
            result_str.append(result)

        return ''.join(result_str)



if __name__ == "__main__":
    sol = Solution()
    print(sol.mapWordWeights(words=["abcd","def","xyz"],
                       weights=[5,3,12,14,1,2,3,2,10,6,6,9,7,8,7,10,8,9,6,9,9,8,3,7,7,2]))