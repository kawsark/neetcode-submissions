# Meta: '{"felt":"medium","time":25,"help":"none"}'
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Add speed to array
        for idx_p in range(len(position)):
            position[idx_p] = (position[idx_p], speed[idx_p])

        position.sort(key=lambda item: item[0])
        #print(f"position is: {position}")

        res = 0
        latest_fleet_arrival_time = None

        for idx_car in range(len(position)-1,-1,-1):
            pos = position[idx_car][0]
            speed = position[idx_car][1]

            d = target - pos
            t = d / speed
        
            if not latest_fleet_arrival_time or t > latest_fleet_arrival_time:
                latest_fleet_arrival_time = t
                res += 1
            # else t > latest_fleet_arrival_time so its part of the prevous fleet
        
        return res


        