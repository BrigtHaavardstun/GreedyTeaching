# This is the manager of the program

from Consistensy_graph.GetAvgDegreeConcept import getAvgDegreeOfRepresentations as getAvgReps
from Consistensy_graph.GetMedianDegreeConcept import getMedianDegreeOfConcepts as getMedConc
from Consistensy_graph.GetAvgDegreeWitness import getAvgDegreeOfWitnesses as getAvgWitness
from Consistensy_graph.GetMedianDegreeWitness import getMedianDegreeOfWitnesses as getMedWitness
from Consistensy_graph.GetRedudencyRate import getRedudencyRate as getRedRate
from Consistensy_graph.GetConceptCount import getNrOfConceptInConsistensyGraph as getConceptCount
from Consistensy_graph.GetRepresentationCount import getNrOfRepresentationsInConsistensyGraph as getRepCount
from Consistensy_graph.GetWitnessCount import getNrOfWitnessSetsInConsistensyGraph as getWitnessCount
from Consistensy_graph.GetEdgePercentage import getEdgePercentage as getEdgePercentage
from Consistensy_graph.GetUniqueness import getUniquenessOfRepresentations as getUniqueness

from MatchingEvaluation.GetNumberConceptTaught import getNrOfConcepts
from MatchingEvaluation.GetNumberRepresentationTaught import getNrOfRepresentations as getNrOfReps
from MatchingEvaluation.GetMaxWitnessSet import get_max_witness_set_size as getMaxWitnessSize
from MatchingEvaluation.GetMaxWitnessNumber import get_max_witness_set_nr as getMaxWitnessNr

from OptimalMatching.FindOptimalMatching import findAndStoreOptimalMatching


def main(folder):
    # makeOptimalMatching(folder)
    graphInfo(folder)
    # matchingInfo(folder)


def makeOptimalMatching(folder):
    print("-"*10 + "Start to create optimal matching..." + "-"*10)
    findAndStoreOptimalMatching(folder)
    print("-"*10 + "Done creating optimal matching" + "-"*10)


def matchingInfo(folder):
    matchings = ["optimal"]  # ["eager", "greedy", "optimal"]
    for matching in matchings:
        print("-"*10 + matching + "-"*10)
        print("Nr. concepts in matching",
              getNrOfConcepts(folder=folder, matching=matching))
        print("Nr. reps. in matching",
              getNrOfReps(folder=folder, matching=matching))
        print("Max witness size", getMaxWitnessSize(
            folder=folder, matching=matching))
        print("Max witness nr", getMaxWitnessNr(
            folder=folder, matching=matching))


def graphInfo(folder):
    print("-"*10 + "Graph Info" + "-"*10)
    print("Nr Concepts:", getConceptCount(folder))
    print("Nr Representations:", getRepCount(folder))
    print("Nr witness sets:", getWitnessCount(folder))

    print("Redudency rate:", str(getRedRate(folder))+"%")

    print("Avg Deg Representations:", getAvgReps(folder))
    # print("Median Deg Concepts:", getMedConc(folder))
    print("Avg Deg Witness:", getAvgWitness(folder))
    # print("Median Deg Witness", getMedWitness(folder))
    print("Percentage of edges in consitency graph:",
          str(getEdgePercentage(folder))+"%")
    print("Uniqueness:", getUniqueness(folder))


if __name__ == "__main__":
    # This is the main program. To run it, insert a folder with the same
    # structure as "boolean" into the project
    # Then update the name here, and run the program

    folderName = "3-DNF_max_cardin_5"
    main(folderName)
