# This is the manager of the program

from Consistensy_graph.GetAvgDegreeConcept import getAvgDegreeOfConcepts as getAvgConc
from Consistensy_graph.GetMedianDegreeConcept import getMedianDegreeOfConcepts as getMedConc
from Consistensy_graph.GetAvgDegreeWitness import getAvgDegreeOfWitnesses as getAvgWitness
from Consistensy_graph.GetMedianDegreeWitness import getMedianDegreeOfWitnesses as getMedWitness
from Consistensy_graph.GetRedudencyRate import getRedudencyRate as getRedRate
from Consistensy_graph.GetConceptCount import getNrOfConceptInConsistensyGraph as getConceptCount
from Consistensy_graph.GetRepresentationCount import getNrOfRepresentationsInConsistensyGraph as getRepCount
from Consistensy_graph.GetWitnessCount import getNrOfWitnessSetsInConsistensyGraph as getWitnessCount

from MatchingEvaluation.GetNumberConceptTaught import getNrOfConcepts
from MatchingEvaluation.GetNumberRepresentationTaught import getNrOfRepresentations as getNrOfReps
from MatchingEvaluation.GetMaxWitnessSet import get_max_witness_set_size as getMaxWitnessSize
from MatchingEvaluation.GetMaxWitnessNumber import get_max_witness_set_nr as getMaxWitnessNr


def get_info_concsitensy_graph():
    concept_number = True
    representation_number = True
    average_degree_witness = True
    average_degree_representation = True
    redudency_precentage = True


def main():
    folder = "boolean"

    # graphInfoTest(folder)
    matchingInfoTest(folder)


def matchingInfoTest(folder):
    matchings = ["eager", "greedy", "optimal"]
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


def graphInfoTest(folder):
    print("Nr Concepts:", getConceptCount(folder))
    print("Nr Representations:", getRepCount(folder))
    print("Nr witness sets:", getWitnessCount(folder))

    print("Redudency rate:", str(getRedRate(folder))+"%")

    print("Avg Deg Concepts:", getAvgConc(folder))
    print("Median Deg Concepts:", getMedConc(folder))
    print("Avg Deg Witness:", getAvgWitness(folder))
    print("Median Deg Witness", getMedWitness(folder))


if __name__ == "__main__":
    main()
