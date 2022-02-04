#Ideal solution
#O(n) time, O(1) space
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #This problem can essentially be visualized by a linked list with a cycle
        #We have at least a pair of duplicate numbers, so a cycle will exist
        #However, in order to find the duplicate element, we much find the start of the starting point of the cycle
        #Say the cycle starts a distance a from the start
        #Our fast and slow pointers meet at a distance b within the cycle, and the distance back to the start is c
        #So, the slow pointer travelled A + B
        #The fast pointer travelled A + 2B + C = 2A + 2B
        #Simplifying, we see A = C
        #Thus, in order to find the start once our pointers meet, we initialize a third dummy pointer at the start of the list, and move the slow pointer and the dummy pointer up one spot each until they are equal
        #When they are equal, we have found the duplicate element
        
        #Normal linked list cycle stuff, find the point where the fast and slow pointers meet
        slow = nums[0]
        fast = nums[slow]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
        #Once this occurs, we then initialize a dummy pointer and keep going
        front = 0
        while slow != front:
            slow = nums[slow]
            front = nums[front]
        return slow 
    
    
#Other solution, more logical
#O(nlog(n)) time, O(1) space
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #We know the numbers in the array range from 1 to len(nums) - 1
        #Perform binary search in that range
        #[1,2,3,4] -> We see that in an idea case, the number of entries less
        #than or equal to any number is that number: Ex for 4, there are 4 numbers <= to 4
        #However: [1,2,3,3]: If the count is greater than that number, we know we have a duplicate
        #So, for each binary search iteration, we can iterate through the array and check to see which half of the curr number contains the duplicate:
        low = 0
        high = len(nums) - 1
        
        #Keep track of the duplicate
        duplicate = -1
        
        while low <= high:
            mid = (low + high) // 2
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            
            if count > mid:
                duplicate = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return duplicate
