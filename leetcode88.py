class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        #Getting the last index of nums1
        last = m + n - 1

        #merging in reverse order

        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n-1]
                n -= 1
            last -= 1

        #filling nums1 with the leftover nums2 elements

        while n > 0:
            nums1[last] = nums2[n - 1] 
            n = n-1
            last = last - 1

