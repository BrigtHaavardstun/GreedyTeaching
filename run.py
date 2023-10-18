# This is the manager of the program


from Consistensy_graph.GetRedudencyRate import getRedudencyRate as getRedRate
from Consistensy_graph.GetConceptCount import getNrOfConceptInConsistensyGraph as getConceptCount
from Consistensy_graph.GetRepresentationCount import getNrOfRepresentationsInConsistensyGraph as getRepCount
from Consistensy_graph.GetWitnessCount import getNrOfWitnessSetsInConsistensyGraph as getWitnessCount
from Consistensy_graph.GetEdgePercentage import getEdgePercentage as getEdgePercentage
from Consistensy_graph.GetUniqueness import getUniquenessOfRepresentations as getUniqueness
from Consistensy_graph.GetWitnessSpread import getWitnessSpread

from MatchingEvaluation.GetNumberConceptTaught import getNrOfConcepts
from MatchingEvaluation.GetNumberRepresentationTaught import getNrOfRepresentations as getNrOfReps
from MatchingEvaluation.GetMaxWitnessSet import get_max_witness_set_size as getMaxWitnessSize
from MatchingEvaluation.GetMaxWitnessNumber import get_max_witness_set_nr as getMaxWitnessNr

from OptimalMatching.FindOptimalMatching import findAndStoreOptimalMatching
from OptimalMatching.ConceptOptimal import findAndStoreNewOptimalMatching


def main(folder):
    makeOptimalMatching(folder)
    graphInfo(folder)
    matchingInfo(folder)


def makeOptimalMatching(folder):
    print("-"*10 + "Start to create optimal matching..." + "-"*10)
    findAndStoreOptimalMatching(folder)
    findAndStoreNewOptimalMatching(folder)
    print("-"*10 + "Done creating optimal matching" + "-"*10)


def matchingInfo(folder):
    # ["eager", "greedy", "optimal"]
    matchings = ["optimal", "optimalNew"]  # , "greedy"]
    for matching in matchings:
        if "optimalNew" == matching:
            print("-"*10 + "Optimal-2 approximation" + "-"*10)
        else:
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

    print("Density:",
          str(getEdgePercentage(folder))+"%")
    print("Redudancy:", round(1-getUniqueness(folder), 4))
    print("Redudancy Spread:", getWitnessSpread(folder))


if __name__ == "__main__":
    # This is the main program. To run it, insert a folder with the same
    # structure as "boolean" into the project
    # Then update the name here, and run the program

    folderName = "sudo-P3"
    print("Working in domain:", folderName)
    main(folderName)
