
# >>>>>>>> Time Limit exceeded and failed <<<<<<<<<< 
# class Solution:
#     def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
#         # point_distance = {}
#         origin = [0, 0]
#         distances = []
#         result = []
#         # calculate distance for each point relative from origin 
#         for x in range(len(points)):
#             point = points[x]
#             distance = ((point[0]-origin[0])**2+(point[1]-origin[1])**2)
#             # point_distance[distance] = point
#             distances.append(distance)
#         # print(point_distance[10])
#         # for x in range(len(point_distance)):
        
#         # Time limit exceeded
#         # sort it out to make it easier in distance incrementally
#         for x in range(len(distances)):
#             min_distance = distances[x]
#             min_point = points[x]
#             for y in range(x+1, len(distances)):
#                 if min_distance > distances[y]:
#                     min_distance, distances[y] = distances[y], min_distance
#                     min_point, points[y] = points[y], min_point    
#             distances[x] = min_distance
#             points[x] = min_point
        
#         # return k number of items
#         for i in range(k):
#             result.append(points[i])
#         return result