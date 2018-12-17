import sys
from Configuration import Configuration
from genetic.Population import Population
from genetic.ChromosomeConfig import ChromosomeConfig
import math
from tsp import tsp

config = Configuration()
config.load('configuration.xml')

TSP = tsp(filePath)
TSP.buildClassifier(TSP.instances)

chromosomeConfig = ChromosomeConfig()
chromosomeConfig.alphaLength = config.alphaLength
chromosomeConfig.alphaInitValue = config.alphaInitValue
chromosomeConfig.betaLength = config.betaLength
chromosomeConfig.betaInitValue = config.betaInitValue
chromosomeConfig.geneLength = math.floor(math.log2(TSP.instances.numAttributes())) + 1

population = Population(config.populationSize)

population.setQualityChecker(TSP.checkFitness(data))
population.fillRandomly(chromosomeConfig, config.comparisonsCount)

#population.print()
for i in range(0, config.evolutionLength):
    population.nextGeneration(config.selectionSize, config.crossingProbability, config.mutationProbability)
    if population.isFound(config.targetProbability):
        break
#population.print()
print('Generation: ' + str(population.generation))
population.printBest()


