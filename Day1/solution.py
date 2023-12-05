import sys

def main():
    input_path = sys.argv[1] #input file path

    partOneSum, partTwoSum = 0, 0
    with open(input_path) as file:
        for line in file:
            partOneSum = partOneSum + getFirstAndLastNumbersPartOne(line.strip()) #strip for sneaky whitespace
            partTwoSum = partTwoSum + getFirstAndLastNumbersPartTwo(line.strip())
        print(f"Part One Sum: {partOneSum}")
        print(f"Part Two Sum: {partTwoSum}")

def getFirstAndLastNumbersPartOne(text: str) -> int:
    firstSet, lastSet = False, False
    firstDigit, lastDigit = 0, 0
    for start_char, end_char in zip(text, reversed(text)):
        if firstSet and lastSet:
            break

        if not firstSet and start_char.isdigit():
            firstDigit = start_char
            firstSet = True

        if not lastSet and end_char.isdigit():
            lastDigit = end_char
            lastSet = True

    return int(str(firstDigit) + str(lastDigit))

def getFirstAndLastNumbersPartTwo(text: str) -> int:
    firstSet, lastSet = False, False
    firstDigit, lastDigit = 0, 0

    for index, char in enumerate(text):
        # no need to keep looking if first and last found
        if firstSet and lastSet:
            break

        if not firstSet:
            if char.isdigit():
                firstDigit = char
                firstSet = True
            else:
               digitFromText = TryGetNumberFromText(text[index:])
               if digitFromText is not None:
                firstDigit = digitFromText
                firstSet = True

        # moving from the end of the string
        if not lastSet:
            if text[(index + 1) * -1].isdigit():
                lastDigit = text[(index + 1) * -1]
                lastSet = True
            else:
               digitFromText = TryGetNumberFromText(text[(len(text) - 1) - index:])
               if digitFromText is not None:
                lastDigit = digitFromText
                lastSet = True
    
    return int(str(firstDigit) + str(lastDigit))

def TryGetNumberFromText(text: str) -> int:
    if text.startswith("zero"):
        return 0
    if text.startswith("one"):
        return 1
    if text.startswith("two"):
        return 2
    if text.startswith("three"):
        return 3
    if text.startswith("four"):
        return 4
    if text.startswith("five"):
        return 5
    if text.startswith("six"):
        return 6
    if text.startswith("seven"):
        return 7
    if text.startswith("eight"):
        return 8
    if text.startswith("nine"):
        return 9
    return None

if __name__ == "__main__":
    main()