class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        total_events = 0
        current_day = 0
        min_heap = []
        
        i = 0
        n = len(events)
        
        # Iterate over days as long as there are events in the heap or events left in the list
        while i < n or min_heap:
            # Move the day to the next relevant event's start day
            if not min_heap:
                current_day = events[i][0]
            
            # Push all events that start on the current day or before into the min-heap
            while i < n and events[i][0] <= current_day:
                heapq.heappush(min_heap, events[i][1])
                i += 1
            
            # Attend the event with the earliest end day
            if min_heap:
                heapq.heappop(min_heap)
                total_events += 1
                current_day += 1  # Move to the next day
            
            # Remove all events from the heap that have already ended
            while min_heap and min_heap[0] < current_day:
                heapq.heappop(min_heap)
        
        return total_events