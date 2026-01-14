class Solution:
    def maxSum(self, nums: List[int]) -> int:
        def max_digit(n):
            return max(int(d) for d in str(n))
        
        # Group numbers by their maximum digit
        groups = {}
        for num in nums:
            digit = max_digit(num)
            if digit not in groups:
                groups[digit] = []
            groups[digit].append(num)
        
        result = -1
        for digit, group in groups.items():
            if len(group) >= 2:
                # Get two largest numbers in this group
                group.sort(reverse=True)
                result = max(result, group[0] + group[1])
        
        return result