class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n: int = len(students) # Equal to len(sandwiches)
        i: int = 0 # Sandwich stack index
        q: int = 0 # Student queue index
        
        for i in range(n): # Students will the sandwich at top of sandwich stack or go hungry
            qlen = n - i
            for j in range(q, qlen + q):
                j = j % qlen
                if sandwiches[i] == students[j]:
                    students.pop(j)
                    q = j
                    break
            if qlen == len(students):
                return qlen
        return 0

