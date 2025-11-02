class WordFinder:
    def set_grid(self, grid):
        self.grid = grid

    def count(self, word):
        count = 0
        
        # count horizontal
        for row in self.grid:
            hor_buffer = ""
            for char in row:
                hor_buffer += char
                if word in hor_buffer or word in hor_buffer[::-1]:
                    count += 1
                    hor_buffer = ""
        
        # count vertical
        ver_buffer = ""
        for i in range(len(self.grid[0])):
            for row in self.grid:
                ver_buffer += row[i]
                if word in ver_buffer or word in ver_buffer[::-1]:
                    count += 1
                    ver_buffer = ""
        
                
        
        return count
            
        

if __name__ == "__main__":
    grid = ["TIRATIRA",
            "IRATIRAT",
            "RATIRATI",
            "ATIRATIR"]

    finder = WordFinder()
    finder.set_grid(grid)

    print(finder.count("TIRA")) # 7 
    print(finder.count("TA")) # 13
    print(finder.count("RITARI")) # 3
    print(finder.count("A")) # 8
    print(finder.count("AA")) # 6
    print(finder.count("RAITA")) # 0  
