class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        self.count = 0
        
        def visit(room):
            if room not in visited:
                visited.add(room)
                self.count += 1
                for key in rooms[room]:
                    visit(key)
        
        visit(0)
        return self.count == len(rooms)
        
