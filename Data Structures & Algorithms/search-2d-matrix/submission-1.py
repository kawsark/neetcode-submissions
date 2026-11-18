# Meta: '{"felt": "Easy", "time": 25, "help": "none", "Comment": "Need to remember the laws of binary search"}'

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        rowlen = len(matrix[0])

        # Locate the row
        while left <= right:
            mid = left + (right - left) // 2
            print(f"Mid is: {mid}")
            left_element = matrix[mid][0]
            right_element = matrix[mid][rowlen - 1]
            if right_element == target:
                return True
            elif target >= left_element and target <= right_element:
                break
            elif target > right_element:
                left = mid + 1
            else: # target < left_element:
                right = mid - 1
        
        left = 0
        right = rowlen - 1
        row = matrix[mid]

        while left <= right:
            mid = left + (right - left) // 2
            if row[mid] == target:
                return True
            elif target > row[mid]:
                left = mid + 1
            else: # target < row[mid]
                right = mid - 1
        
        return False

        