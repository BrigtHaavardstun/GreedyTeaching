# Analysis of Experiment Results

This repository provides tools for analyzing different algorithms, as used in the paper _When Redundancy Matters: Machine Teaching (of) Representations_.

## 📂 How to Use

### 1. Install Dependencies

Install the necessary dependencies as per `requirements.txt`. These include:
- `networkx`

You can install them using pip:
```bash
pip install -r requirements.txt
```

or 
```
pip install networkx
```
### 2. Modify `run.py`

Open `run.py` and insert the name of your folder on line 69., chose on of the folders in the project
- small-P3
- 3-DNF_max_cardin_5
- 3-Term_DNF_max_cardin_5


### 3. Run `run.py`
```bash
python3 run.py
```

### 4. (Extra) Adding your own Data Folder

You can use the system developed here 
Upload a folder with a name of your choice (e.g., "MyFolder") to the folder Data. Ensure it contains the following files:

- **a.** `eager-matching.json` (optional) - Matching created by the eager algorithm.
    - Format: `[[representationID, witnessID]]`
- **b.** `greedy-matching.json` (optional) - Matching created by the greedy algorithm.
    - Format: `[[representationID, witnessID]]`
- **c.** `graph-edges.json` - The consistency graph for your domain.
    - Format: Edgelist `[[representationID, witnessID]]`
- **d.** `graph-representations.json` - Dictionary containing information on the representations.
    - Format: `{representationID : [representation, size]}`
- **e.** `graph-witness_sets.json` - Dictionary containing information on the witness sets.
    - Format: `{witnessID : [witnessSet, size]}`

  
**Note:** `representationID` should start with "c_" and `witnessID` should start with "w_".




