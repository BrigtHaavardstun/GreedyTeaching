# Analysis of Experiment Results

This repository provides tools for analyzing different algorithms, as used in the paper _When Redundancy Matters: Machine Teaching (of) Representations_.

## 📂 How to Use

### 1. Prepare Your Data Folder

Upload a folder with a name of your choice (e.g., "MyFolder"). Ensure it contains the following files:

  a. `eager-matching.json` - Matching created by the eager algorithm.
     - Format: `[[representationID, witnessID]]`
  b. `greedy-matching.json` - Matching created by the greedy algorithm.
     - Format: `[[representationID, witnessID]]`
  c. `graph-edges.json` - The consistency graph for your domain.
     - Format: Edgelist `[[representationID, witnessID]]`
  d. `graph-representations.json` - Dictionary containing information on the representations.
     - Format: `{representationID : [representation, size]}`
  e. `graph-witness-sets.json` - Dictionary containing information on the witness sets.
     - Format: `{witnessID : [witnessSet, size]}`
  
**Note:** `representationID` should start with "c_" and `witnessID` should start with "w_".

### 2. Modify `run.py`

Open `run.py` and insert the name of your folder (e.g., "MyFolder") on line 65.

### 3. Install Dependencies

Install the necessary dependencies as per `requirements.txt`. From the information available, these include:
- `networkx`
- `json`

You can install them using pip:
```bash
pip install -r requirements.txt
