class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        pref_zero = students.count(0)
        pref_one = len(students) - pref_zero

        for s in sandwiches:
            if s == 0:
                if pref_zero == 0:
                    return pref_zero + pref_one
                pref_zero -= 1
            else:
                if pref_one == 0:
                    return pref_zero + pref_one
                pref_one -= 1
        
        return 0
        

