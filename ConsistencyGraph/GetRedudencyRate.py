from Consistensy_graph.GetConceptCount import getNrOfConceptInConsistensyGraph as nrConcepts
from Consistensy_graph.GetRepresentationCount import getNrOfRepresentationsInConsistensyGraph as nrRepresentations


# Thus far, redudency -> 1-(concepts/representations)
def getRedudencyRate(folder):
    return round(100*(1-nrConcepts(folder)/nrRepresentations(folder)), 2)
