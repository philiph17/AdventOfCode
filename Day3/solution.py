import sys

def main():
    input_path = sys.argv[1] #input file path

    previousLine = ""
    with open(input_path) as file:
        for line in file:

            previousLine = line
            return True


def findNeighbors(matrix, target): #List<(int, int)> 

    neighbors = []
    directions = [ 
        (-1, -1), # Top Left
        (-1, 0), # Top
        (-1, 1), # Top Right
        (0, -1), #Left
        (0, 1)   #Right
        (1, -1),  # Bottom Left
        (1, 0),  # Bottom
        (1, 1),  # Bottom Right
        ]
    
    for i in range(0, len(matrix) - 1):
        for j in range(0, len(matrix[i]) - 1):
            if (matrix[i][j] == target):
                for direction in directions:
                    dx, dy = direction
                    newX = i + dx
                    newY = j + dy
                    if (newX >= 0 and newX < matrix.Length and newY >= 0 and newY < matrix[i].Length):
                        neighbors.append((newX, newY))

    return neighbors

if __name__ == "__main__":
    main()