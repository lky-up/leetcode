"""
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
你可以假设 nums1 和 nums2 不会同时为空。
示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
思路参考：https://www.cnblogs.com/yinbiao/articles/11278881.html
"""

class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:

        m = len(nums1)
        n = len(nums2)
        if m>n:
            m,n,nums1,nums2 = n,m,nums2,nums1
        imax = m
        imin = 0
        half_ls = int((m+n+1)/2)
        while imin<=imax:
            i = int((imax+imin)/2)
            j = half_ls - i
            if i < m and nums1[i]<nums2[j-1]:
                imin = i + 1
            elif i > 0 and nums1[i-1]>nums2[j]:
                imax = i - 1
            else:
                if i == 0:
                    max_left = nums2[j-1]
                elif j == 0:
                    max_left  = nums1[i-1]
                else:
                    max_left = max(nums1[i-1],nums2[j-1])
                if (m+n)%2 == 1:
                    return max_left
                if i == m:
                    min_right = nums2[j]
                elif j == n:
                    min_right = nums1[i]
                else:
                    min_right = min(nums1[i],nums2[j])
                return (max_left+min_right)/2.0


