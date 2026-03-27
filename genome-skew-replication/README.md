# Genome Skew & Replication Origin Analysis

Computes GC skew across a genome and identifies the replication origin (oriC) using two complementary methods: minimum skew position and clump finding.

**Why it matters:** During DNA replication, cytosine (C) on the lagging strand deaminates to uracil more frequently, causing an asymmetry in G vs C count across the genome. The position where skew is at its minimum marks the likely origin of replication — a critical target in microbiology and synthetic biology.

## Scripts

| Script | Description |
|---|---|
| `min_skew.py` | Computes running GC skew (G−C) across the genome and returns positions of minimum skew — the predicted oriC location |
| `clump.py` | Finds all k-mers appearing at least t times within any window of length L — another method to identify replication origin candidates |

## Usage

```bash
python min_skew.py
# Enter a genome: CCTATCGGTGGATTAGCATGTCCCTGTACGTTTCGCCGCGTATCCGGCTTCAATCTTCA
# Returns positions of minimum skew

python clump.py
# Enter the sequence: CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGACATTGCGACATAATGTACGAATGTAATGTGCCTATGGC
# Enter the kmer: 5
# Enter the clump L: 75
# Enter the minimum requirement t: 4
# CGACA GAAGA AATGT
```

## Dependencies

No external dependencies — standard Python only.
