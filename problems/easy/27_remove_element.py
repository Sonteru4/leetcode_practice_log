"""
LeetCode Problem: Remove Element

Problem Statement:
-----------------
You are given an integer array nums and an integer val. Your task is to remove 
all occurrences of val from nums in-place.

After removing all occurrences of val, return the number of remaining elements, 
say k, such that the first k elements of nums do not contain val.

Note:
- The order of the elements which are not equal to val does not matter.
- It is not necessary to consider elements beyond the first k positions of the array.
- To be accepted, the first k elements of nums must contain only elements not equal to val.
- Return k as the final result.

Example 1:
----------
Input: nums = [1,1,2,3,4], val = 1
Output: [2,3,4]
Explanation: You should return k = 3 as we have 3 elements which are not equal to val = 1.

Example 2:
----------
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: [0,1,3,0,4]
Explanation: You should return k = 5 as we have 5 elements which are not equal to val = 2.

Constraints:
-----------
- 0 <= nums.length <= 100
- 0 <= nums[i] <= 50
- 0 <= val <= 100
"""


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        """
        Remove all occurrences of val from nums in-place using two-pointer technique.
        
        Time Complexity: O(n) - we iterate through the array once
        Space Complexity: O(1) - we modify the array in-place without extra space
        
        Args:
            nums: List of integers to modify in-place
            val: Value to remove from the list
            
        Returns:
            k: Number of elements in nums which are not equal to val
        """
        # k tracks the position where we should place the next non-val element
        k = 0
        
        # Iterate through all elements in the array
        for i in range(len(nums)):
            # If current element is not equal to val, keep it
            if nums[i] != val:
                # Place the element at position k
                nums[k] = nums[i]
                # Increment k to point to next available position
                k += 1
        
        # k now represents the count of elements not equal to val
        return k


"""
Detailed Explanation:
--------------------

Algorithm: Two-Pointer Technique
--------------------------------
This solution uses a two-pointer approach:
1. Pointer 'k' - tracks where to place the next valid (non-val) element
2. Pointer 'i' - scans through the entire array

How it works:
-------------
1. Initialize k = 0 (position for next valid element)
2. Loop through array with index i:
   - If nums[i] != val: it's a valid element
     * Copy it to position k: nums[k] = nums[i]
     * Increment k to prepare for next valid element
   - If nums[i] == val: skip it (don't increment k)
3. Return k (count of valid elements)

Visual Example:
--------------
nums = [0,1,2,2,3,0,4,2], val = 2

Step-by-step execution:
i=0: nums[0]=0 != 2 → nums[0]=0, k=1  [0,1,2,2,3,0,4,2]
i=1: nums[1]=1 != 2 → nums[1]=1, k=2  [0,1,2,2,3,0,4,2]
i=2: nums[2]=2 == 2 → skip             [0,1,2,2,3,0,4,2]
i=3: nums[3]=2 == 2 → skip             [0,1,2,2,3,0,4,2]
i=4: nums[4]=3 != 2 → nums[2]=3, k=3  [0,1,3,2,3,0,4,2]
i=5: nums[5]=0 != 2 → nums[3]=0, k=4  [0,1,3,0,3,0,4,2]
i=6: nums[6]=4 != 2 → nums[4]=4, k=5  [0,1,3,0,4,0,4,2]
i=7: nums[7]=2 == 2 → skip             [0,1,3,0,4,0,4,2]

Final: k=5, first 5 elements are [0,1,3,0,4]

Key Insights:
------------
1. We don't need to preserve order of elements
2. We only care about first k elements being valid
3. Elements after position k can be anything
4. In-place modification saves memory
5. Single pass through array makes it efficient

Edge Cases:
----------
- Empty array: returns 0
- All elements equal to val: returns 0
- No elements equal to val: returns original length
- Single element array: returns 0 or 1
"""


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums1 = [1, 1, 2, 3, 4]
    val1 = 1
    k1 = solution.removeElement(nums1, val1)
    print(f"Test 1: k = {k1}, nums = {nums1[:k1]}")  # Expected: k=3, nums=[2,3,4]
    
    # Test case 2
    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    val2 = 2
    k2 = solution.removeElement(nums2, val2)
    print(f"Test 2: k = {k2}, nums = {nums2[:k2]}")  # Expected: k=5, nums=[0,1,3,0,4]
    
    # Test case 3: Empty array
    nums3 = []
    val3 = 1
    k3 = solution.removeElement(nums3, val3)
    print(f"Test 3: k = {k3}, nums = {nums3[:k3]}")  # Expected: k=0, nums=[]
    
    # Test case 4: All elements equal to val
    nums4 = [2, 2, 2, 2]
    val4 = 2
    k4 = solution.removeElement(nums4, val4)
    print(f"Test 4: k = {k4}, nums = {nums4[:k4]}")  # Expected: k=0, nums=[]
    
    # Test case 5: No elements equal to val
    nums5 = [1, 2, 3, 4]
    val5 = 5
    k5 = solution.removeElement(nums5, val5)
    print(f"Test 5: k = {k5}, nums = {nums5[:k5]}")  # Expected: k=4, nums=[1,2,3,4]
