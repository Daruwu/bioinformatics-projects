# Approximate Pattern Matching with Hamming Distance

Identifies where a DNA pattern occurs in a genome when allowing for a set number of mismatches (d). Uses Hamming distance — the number of positions where two strings differ — as the mismatch metric.

**Why it matters:** Real biological sequences contain mutations, sequencing errors, and SNPs. Exact matching misses these. Approximate matching with a mismatch tolerance is essential for primer design, mutation detection, and binding site identification.

## Scripts

| Script | Description |
|---|---|
| `hamming_dist.py` | Computes the Hamming distance between two equal-length sequences |
| `Approx_Pat_Match.py` | Finds all positions in a genome where a pattern appears with at most d mismatches. Includes frequency analysis, skew computation, and symbol arrays |
| `test_code.py` | Extended test version of approximate matching with additional helper functions |

## Usage

```bash
python hamming_dist.py
# Enter first sequence:  GGGCCGTTGGT
# Enter second sequence: GGACCGTTGAC
# 3

python Approx_Pat_Match.py
# Enter a pattern: ATTCTGGA
# Enter a sequence: CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT
# Enter a d-value: 3
# 6 7 26 31
```

## Dependencies

```bash
pip install biopython
```
