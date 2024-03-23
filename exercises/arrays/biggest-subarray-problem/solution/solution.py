class Solution:
	def findMaximumSubarray(self, nums: list[int]) -> int:
		maximum_sum = nums[0]
		current_sum = nums[0]
		print(f"Initial Maximum Sum: {maximum_sum}, Current Sum: {current_sum}")	
		for num in nums[1:]:
			current_sum = max(num, current_sum + num)
			maximum_sum = max(maximum_sum, current_sum)
			print(f"Current Sum: {current_sum}, Maximum Sum: {maximum_sum}")
		print(f"Final Maximum Sum: {maximum_sum}")
		return maximum_sum		
