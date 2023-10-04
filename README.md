# Analysis of experiment results
Tools used to analyse the different algorithms for the paper When Redundancy Matters: Machine Teaching (of) Representations.

How to use:
    1. Upload a folder with a name of your choice, i.e. "MyFolder". The folder must contain the following files:
        a. eager-matching.json - The matching created by eager algorithm. Format [[representationID, witnessID]]
        b. greedy-matching.json - The matching created by greedy algorithm. Format [[representationID, witnessID]]
        c. graph-edges.json - The consistency graph on your domain. Format edgelist, [[representationID, witnessID]]
        d. graph-representations.json - The dict containing info on the representations. Format {representationID : [representation, size]}.
        e. graph-witness-sets.json - The dict containing info on the witness sets. Format {witnessID : [witnessSet, size]}.
        NB: representationID must start with "c_" and witnessID must start with "w_".

    2. In run.py, insert the name of your folder, i.e. "MyFolder" on the 65'th line.
    3. Install the requirements (see requirements.txt), (as far as i recalll it is just networkx and json)
    4. Run run.py

    
        

