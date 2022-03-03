class Solution:
    def __init__(self):
        self.startingPixel = None
        self.counter = 0
        self.seen = set()
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if self.counter == 0:
            self.startingPixel = image[sr][sc]
        self.counter += 1
        
        if image[sr][sc] == self.startingPixel:
            if (sr, sc) in self.seen:
                return 
            self.seen.add((sr,sc))
            image[sr][sc] = newColor
            
            if sr-1 >= 0 and image[sr-1][sc] == self.startingPixel:
                self.floodFill(image, sr-1, sc, newColor)

            if sr+1 < len(image) and image[sr+1][sc] == self.startingPixel:
                self.floodFill(image, sr+1, sc, newColor)

            if sc-1 >= 0 and image[sr][sc-1] == self.startingPixel:
                self.floodFill(image, sr, sc-1, newColor)

            if sc+1 < len(image[0]) and image[sr][sc+1] == self.startingPixel:
                self.floodFill(image, sr, sc+1, newColor)

            
        return image