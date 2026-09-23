class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:

        freq = {}

        # Count frequency of nums1
        for num in nums1:
            freq[num] = freq.get(num, 0) + 1

        result = []

        # Find common elements
        for num in nums2:
            if freq.get(num, 0) > 0:
                result.append(num)
                freq[num] -= 1

        return result