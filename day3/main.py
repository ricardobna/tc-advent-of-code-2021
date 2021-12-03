import numpy as np
#gets diagnostics information from input file
input = open('input', 'r')
diagnostics = input.readlines()

gammaRateOnFirst = 0
epsilonRateOnSecond = 0
occurrenceOfOnes = np.zeros(len(diagnostics[0]) - 1)

for diagnostic in diagnostics:
    diagnosticArray = [int(i) for i in list(diagnostic[0:len(occurrenceOfOnes)])]
    occurrenceOfOnes =  np.add(occurrenceOfOnes, diagnosticArray)

def calculateIfOccurrenceOfOnesIsMostCommon(index):
    return 1 if occurrenceOfOnes[index] >= len(diagnostics) // 2 + len(diagnostics) % 2 else 0


def calculateIfOccurrenceOfOnesIsNotMostCommon(index):
    return 1 if occurrenceOfOnes[index] < len(diagnostics) // 2 + len(diagnostics) % 2 else 0

print(occurrenceOfOnes)

gammaRate = 0
gammaRate = calculateIfOccurrenceOfOnesIsMostCommon(0) | gammaRate
epsilonRate = 0
epsilonRate = calculateIfOccurrenceOfOnesIsNotMostCommon(0) | epsilonRate
for  i in range(1,12):
    gammaRate = calculateIfOccurrenceOfOnesIsMostCommon(i) | (gammaRate << 1)
    epsilonRate = calculateIfOccurrenceOfOnesIsNotMostCommon(i) | (epsilonRate << 1)

print(gammaRate * epsilonRate)