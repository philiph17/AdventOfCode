import sys

def main():
    input_path = sys.argv[1] #input file path
    
    gameNumberSum = 0
    minCubePowerSum = 0
    with open(input_path) as file:
        for line in file:
            gameNumber, games = line.split(":")
            if isValidGamePartOne(games):
                gameNumberSum = gameNumberSum + int(gameNumber.split()[-1])
            
            linePower = getPowerOfMinRequiredCubesPartTwo(games)
            minCubePowerSum = minCubePowerSum + linePower

    print(gameNumberSum)
    print(minCubePowerSum)

def isValidGamePartOne(text: str) -> bool:
    for game in text.split(";"):
        for set in game.split(","):
            count, colour = set.split()
            if int(count) > {"red":12,"green":13,"blue":14}[colour]:
                return False
           
    return True

def getPowerOfMinRequiredCubesPartTwo(text: str) -> int:
    red, green, blue = 1, 1, 1
    
    for game in text.split(";"):
        for set in game.split(","):
            count, colour = set.split()
            count = int(count)
            if colour == "red":
                red = max(red, count)
                continue
            if colour == "green":
                green = max(green, count)
                continue
            if colour == "blue":
                blue = max(blue, count)
                continue
           
    return red * green * blue

if __name__ == "__main__":
    main()