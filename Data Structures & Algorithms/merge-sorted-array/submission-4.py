class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j = m - 1, m + n - 1

        while i >= 0:
            if n > 0 and nums2[n - 1] > nums1[i]:
                nums1[j] = nums2[n - 1]
                n -= 1
                j -= 1
            else:
                nums1[j] = nums1[i]
                i -= 1
                j -= 1

        while j >= 0:
            nums1[j] = nums2[j]
            j -= 1
        