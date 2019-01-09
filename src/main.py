import sys
import os
from Configuration import Configuration
from genetic.Population import Population
from genetic.ChromosomeConfig import ChromosomeConfig
import math
import time
from tsp.models.tsp import TSP

config = Configuration()
config.load('configuration.xml')

filePath = config.defaultFilePath
testFilePath = config.defaultTestFilePath

#read filepath from command prompt with no spaces
if len(sys.argv) > 2:
    filePath = sys.argv[1]
    testFilePath = sys.argv[2]

if not os.path.exists(filePath):
     raise Exception('File does not exists')
  
TSP1 = TSP(filePath, config.gamma)
TSP1.buildClassifier(TSP1.instances)

chromosomeConfig = ChromosomeConfig()
chromosomeConfig.alphaLength = config.alphaLength
chromosomeConfig.alphaInitValue = config.alphaInitValue
chromosomeConfig.betaLength = config.betaLength
chromosomeConfig.betaInitValue = config.betaInitValue
chromosomeConfig.geneLength = math.floor(math.log2(TSP1.maxValueOfGene)) #+ 1
chromosomeConfig.compLength = config.compLength

population = Population(config.selectionSize, config.selectionType)

population.setQualityChecker(TSP1.checkFitness)
population.fillRandomly(chromosomeConfig, config.comparisonsCount)


start_time = time.time()
#population.print()
for i in range(0, config.evolutionLength):
    population.nextGeneration(config.crossingProbability, config.mutationProbability)
    if population.isFound(config.targetProbability):
        break
#population.print()
print('Generation: ' + str(population.generation))
best = population.printBest()
print('TIME: ' + str(round(time.time() - start_time, 2)))

TSP2 = TSP(testFilePath, config.gamma)
TSP2.buildClassifier(TSP2.instances)
print('Test score is: ' + str(TSP2.checkFitness(best.toReadableForm())) + '%')
