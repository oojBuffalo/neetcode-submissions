class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        num_hungry: int = len(students)
        pref_count: Counter = Counter(students)

        for s in sandwiches:
            if pref_count[s] > 0:
                num_hungry -= 1
                pref_count[s] -= 1
            else:
                break
        
        return num_hungry
        

