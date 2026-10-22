class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # Sort array
        people.sort()
        left = 0
        right = len(people) - 1
        boats = 0
        person = 0

        # 1,2,2,3,3

        while left < right:
            w = people[left] + people[right]            
            if w <= limit:
                print(f"Adding {people[left]} and {people[right]} to 1 boat")
                person += 2
                left += 1
                right -= 1
            else:
                print(f"Adding {people[right]} to 1 boat")
                person += 1
                right -= 1
            
            boats += 1
        
        while person < len(people):
            boats += 1
            person += 1
        
        return boats