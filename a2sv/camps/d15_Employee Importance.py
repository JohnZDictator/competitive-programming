"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def __init__(self):
        self.importance = 0
        self.subordinates = []
        
    def getImportance(self, employees: List['Employee'], id: int) -> int:
    
        for employee in employees:
            
            if employee.id == id:
                self.dfsSubordinates = [employee]
                
                while len(self.dfsSubordinates) > 0:
                    emp = self.dfsSubordinates.pop()
                    self.importance += emp.importance
                    for employee in employees:
                        if employee.id in emp.subordinates:
                            self.dfsSubordinates.append(employee)
        
                return self.importance