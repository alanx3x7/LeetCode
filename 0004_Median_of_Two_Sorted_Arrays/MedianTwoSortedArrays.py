class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # Set A as the larger list
        if len(nums1) > len(nums2):
            A = nums1
            B = nums2
        else:
            A = nums2
            B = nums1

        # Some values
        total_half = (len(A) + len(B)) // 2
        min_index = total_half - len(B)
        max_index = min(len(A), total_half)

        while 1 == 1:
            A_index = (min_index + max_index) // 2
            B_index = total_half - A_index

            if B_index < len(B) and A[A_index - 1] > B[B_index]:
                max_index = A_index - 1
            elif B_index > 0 and B[B_index - 1] > A[A_index]:
                min_index = A_index + 1
            else:

                if A_index == len(A):
                    min_right = B[B_index]
                elif B_index == len(B):
                    min_right = A[A_index]
                else:
                    min_right = min(A[A_index], B[B_index])

                if (len(A) + len(B)) % 2 == 1:
                    return min_right

                if A_index == 0:
                    max_left = B[total_half - 1]
                elif B_index == 0:
                    max_left = A[total_half - 1]
                else:
                    max_left = max(A[A_index - 1], B[B_index - 1])

                return (max_left + min_right) / 2.0
