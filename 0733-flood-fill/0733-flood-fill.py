class Solution:
    def solve(self, i, j, image, oldcolor, newcolor):
        if i < 0 or j < 0 or i >= len(image) or j >= len(image[0]):
            return

        if image[i][j] != oldcolor:
            return
        
        image[i][j] = newcolor

        self.solve(i - 1, j, image, oldcolor, newcolor)
        self.solve(i + 1, j, image, oldcolor, newcolor)
        self.solve(i, j - 1, image, oldcolor, newcolor)
        self.solve(i, j + 1, image, oldcolor, newcolor)

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        oldcolor = image[sr][sc]

        if oldcolor == color:
            return image

        self.solve(sr, sc, image, oldcolor, color)

        return image