class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        sq_dists= []
        result = []
        
        for i in range(len(points)):
            sq_dist = self.squared_distance(points[i])
            sq_dists.append(sq_dist)
        
        for i in range(k):
            min_dist_index = sq_dists.index(min(sq_dists))
            result.append(points[min_dist_index])
            sq_dists.pop(min_dist_index)
            points.pop(min_dist_index)
            
            
        return result
       
    def squared_distance(self, point: List[int]) -> int:
        return point[0]**2 + point[1]**2