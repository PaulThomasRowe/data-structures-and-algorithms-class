from collections import deque

class Solution:
    def maximumSubarray(self, nums: list[int], k: int) -> list[int]:
        if not nums or k <= 0:
            return []
        
        result = []
        window = deque()
        
        for i, num in enumerate(nums):
            while window and nums[window[-1]] < num: #removing from the right
                window.pop()
                print("Popped from the front.")
            window.append(i) #adding to the right
            print(f"Added {i}.")
            if i - window[0] >= k: #removing from the left
                window.popleft()
                print("Popped from the back.")
            if i >= k - 1: #adding to the result once we've iterated the first index
                result.append(nums[window[0]])
                print(f"Added result {window[0]}.") 
            print(f"Result: {result}, Window: {window}")

        return result
