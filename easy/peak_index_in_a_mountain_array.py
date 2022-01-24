#My solution
#O(n) time, O(1) space
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        #Strategy: Simply find the index of the max value in the array
        for i in range(1, len(arr) - 1):
            if arr[i - 1] < arr[i] and arr[i] > arr[i + 1]:
                return i
        
#Ideal solution
#O(log(n)) time, O(1) space
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        #Strategy: Perform modified binary search. Check if the mid index is a peak, and if it is, return it. Otherwise, we check if the midpoint is on the left of the peak or the right of the peak
        #If the midpoint is on the right of the peak, the val before it will be greater and the val after it will be less. We thus shift the end index back
        #Opposite applies for the left side of the peak
        
        start = 0
        end = len(arr) - 1
        
        while start <= end:
            mid = (start + end) // 2
            if arr[mid - 1] < arr[mid] and arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid -1] > arr[mid] and arr[mid] > arr[mid + 1]:
                end -= 1
            else:
                start += 1
