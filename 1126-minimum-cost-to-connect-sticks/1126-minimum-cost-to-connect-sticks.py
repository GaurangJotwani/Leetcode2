class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        if len(sticks) <= 1:
            return 0  # No cost if there's only one stick
    
        heapq.heapify(sticks)  # Convert sticks list to a min-heap
        total_cost = 0
        
        while len(sticks) > 1:
            # Pop the two smallest sticks
            stick1 = heapq.heappop(sticks)
            stick2 = heapq.heappop(sticks)
            
            # Calculate cost to combine these sticks
            cost = stick1 + stick2
            total_cost += cost
            
            # Push the combined stick back into the heap
            heapq.heappush(sticks, cost)
        
        return total_cost