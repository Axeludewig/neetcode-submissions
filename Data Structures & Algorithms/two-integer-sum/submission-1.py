class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # a map of the number iterated, and its index. {num: index}

        print(enumerate(nums))
        for i, num in enumerate(nums):
            complement = target - num

            print(i, num)
            print(f"The complement of {num} is {complement}")
    
            if complement in seen:

                print(seen[complement])
                print(i)

                return [seen[complement], i]

            seen[num] = i
            print(f"The number {num} doesn't exist on the map so we're adding it")
            print(f"New map: {seen}")