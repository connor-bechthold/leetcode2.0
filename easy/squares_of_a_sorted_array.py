#Brute force
#O(nlog(n)) time, O(1) space
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #Square each val in list, and then sort
        for i in range(0, len(nums)):
            nums[i] = nums[i] ** 2
        nums.sort()
        return nums
    
# My solution
# O(n) time, O(1) space
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #Assign the first index to the smallest absoluted value in the list, or the end of the array
        #Add this value to the returned array
        #Then, initialize another pointer to the left of that value, and assign the orignal pointer to the right of that value
        #Working outwards, add the smallest absoluted value to the returned array, and move that pointer inwards/outwards each time
        #Once one of the pointers reaches the end, we simply add the values infront or behind the remaining pointer to the list, and return
        i = j = 0 
        arr = []
        while i != len(nums) - 1:
            if abs(nums[i]) < abs(nums[i + 1]):
                break;
            i += 1
        arr.append(nums[i] ** 2)
        j = i - 1
        i += 1
        while i < len(nums) and j >= 0:
            if abs(nums[i]) <= abs(nums[j]):
                arr.append(nums[i] ** 2)
                i += 1
            else:
                arr.append(nums[j] ** 2)
                j -= 1
        
        while i < len(nums):
            arr.append(nums[i] ** 2)
            i += 1
            
        while j >= 0:
            arr.append(nums[j] ** 2)
            j -= 1
        
        return arr
    
#Ideal solution
#O(n) time, O(n) space
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #We can start at the front and back of the list, and compare the absolute val of the two nums
        #Whatever is the biggest num will get added to the end of the returned list (sqaured), and we move the pointer of the greater number inwards
        
        arr = [0] * len(nums)
        i = 0
        j = len(nums) - 1
        
        for c in range(len(nums) - 1, -1, -1):
            if abs(nums[i]) >= abs(nums[j]):
                arr[c] = nums[i] ** 2
                i += 1
            else:
                arr[c] = nums[j] ** 2
                j -= 1
                
        return arr
