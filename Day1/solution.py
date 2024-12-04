import sys

def main():
    input_path = sys.argv[1] #input file path

    with open(input_path, 'r') as file:
        part1(file.readlines())
        file.seek(0)
        part2(file.readlines())

def part1(fileLines):
    left = []
    right = []

    for line in fileLines:
        lhs, rhs = (int(s) for s in line.split())
        left.append(lhs)
        right.append(rhs)

    left.sort()
    right.sort()

    diffs = []
    for i, x in enumerate(left):
        diffs.append(abs(x - right[i]))
        
    print(sum(diffs))

def part2(fileLines):
    left = []
    right = []

    for line in fileLines:
        lhs, rhs = (int(s) for s in line.split())
        left.append(lhs)
        right.append(rhs)

    leftElementCounts = {}
    sum = 0
    for l in left:
        if l not in leftElementCounts:
            leftElementCounts[l] = right.count(l)

        sum += l * leftElementCounts[l]
        
    print(sum)

if __name__ == "__main__":
    main()