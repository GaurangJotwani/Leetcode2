# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:

        c_answer = 0
        
        for i in range(1,n):
            if knows(c_answer,i):
                c_answer = i
        
        for i in range(n):
            if c_answer == i:
                continue
            if knows(c_answer, i) or not knows(i, c_answer):
                return -1



        return c_answer
            
            

        