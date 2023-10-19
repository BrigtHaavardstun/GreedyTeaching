# Analysis of Experiment Results

This repository provides tools for analyzing different algorithms, as used in the paper _When Redundancy Matters: Machine Teaching (of) Representations_.

## 📂 How to Use

### 1. Prepare Your Data Folder

Upload a folder with a name of your choice (e.g., "MyFolder"). Ensure it contains the following files:

- **a.** `eager-matching.json` - Matching created by the eager algorithm.
    - Format: `[[representationID, witnessID]]`
- **b.** `greedy-matching.json` - Matching created by the greedy algorithm.
    - Format: `[[representationID, witnessID]]`
- **c.** `graph-edges.json` - The consistency graph for your domain.
    - Format: Edgelist `[[representationID, witnessID]]`
- **d.** `graph-representations.json` - Dictionary containing information on the representations.
    - Format: `{representationID : [representation, size]}`
- **e.** `graph-witness-sets.json` - Dictionary containing information on the witness sets.
    - Format: `{witnessID : [witnessSet, size]}`

  
**Note:** `representationID` should start with "c_" and `witnessID` should start with "w_".



### 2. Install Dependencies

Install the necessary dependencies as per `requirements.txt`. These include:
- `networkx`
- `json`

You can install them using pip:
```bash
pip install -r requirements.txt
```
### 3. Modify `run.py`

Open `run.py` and insert the name of your folder (e.g., "MyFolder") on line 65.
If you want to test the system on a mock domain, use "boolean" as your folder.

### 4. Run `run.py`
```bash
python3 run.py
```



