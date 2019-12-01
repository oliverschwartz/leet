class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        # Check if any individual trip carries more people than the capacity.
        for trip in trips:
            if trip[0] > capacity: 
                return False
        
        # Sort trips by their starting point
        trips.sort(key=lambda trip: trip[1])
        ongoing = set()
        pplCount = 0
        
        # Maintain a set of currently executing trips.
        # Add and remove trips accordingly.
        for i, trip in enumerate(trips):
            ongoing.add(i)
            to_remove = []
            
            for j in ongoing:
                if i == j:
                    pplCount += trip[0]
                elif trips[j][2] <= trip[1]:
                    to_remove.append(j)
                    pplCount -= trips[j][0]
            
            for j in to_remove:
                ongoing.remove(j)
            
            if pplCount > capacity:
                return False
        
        return True
