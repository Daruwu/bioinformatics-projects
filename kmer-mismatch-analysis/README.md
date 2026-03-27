# k-mer Neighborhood & Mismatch Analysis

Generates all k-mer variants within a given Hamming distance (the "neighborhood") and identifies the most frequent k-mers in a sequence when accounting for mismatches and reverse complements.

**Why it matters:** Transcription factor binding sites and replication origin sequences often appear in slightly mutated forms across a genome. Mismatch-tolerant frequency analysis finds these patterns that exact matching would miss.

## Scripts

| Script | Description |
|---|---|
| `d_neighbor.py` | Generates all k-mers within Hamming distance d of a given pattern |
| `fr_words_mis.py` | Finds the most frequent k-mers with up to d mismatches in a sequence |
| `fr_mis_rev.py` | Finds the most frequent k-mers with mismatches AND their reverse complements |

## Usage

```bash
python d_neighbor.py
# Enter a pattern: ACG
# Enter the distance: 1
# Returns all 3-mers within Hamming distance 1 of ACG

python fr_words_mis.py
# Enter a seq: ACGTTGCATGTCGCATGATGCATGAGAGCT
# Enter a k-mer: 4
# Enter a d: 1
# ATGC ATGT

python fr_mis_rev.py
# Enter a sequence: ACGTTGCATGTCGCATGATGCATGAGAGCT
# Enter a k-mer: 4
# Enter a d: 1
# ATGT ACAT
```

## Dependencies

No external dependencies — standard Python only.
