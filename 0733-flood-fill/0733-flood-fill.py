class Solution:
    def solve(self, r, c, image, oldcolor, newcolor):
        if r < 0 or c < 0 or r >= len(image) or c >= len(image[0]):
            return

        if image[r][c] != oldcolor:
            return
        
        image[r][c] = newcolor

        self.solve(r - 1, c, image, oldcolor, newcolor)
        self.solve(r + 1, c, image, oldcolor, newcolor)
        self.solve(r, c - 1, image, oldcolor, newcolor)
        self.solve(r, c + 1, image, oldcolor, newcolor)

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        oldcolor = image[sr][sc]

        if oldcolor == color:
            return image

        self.solve(sr, sc, image, oldcolor, color)

        return image