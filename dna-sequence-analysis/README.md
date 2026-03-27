# DNA Sequence Analysis Toolkit

Core command-line tools for analyzing raw DNA sequences. Built from scratch to understand the underlying biology and algorithms before leveraging higher-level libraries.

## Scripts

| Script | Description |
|---|---|
| `side_project.py` | Counts each nucleotide (A, T, G, C) in a user-supplied DNA sequence |
| `seq.py` | Nucleotide counts on a hardcoded sequence using BioPython's `Seq` object |
| `frequent_words.py` | Finds the most frequently occurring k-mers in a sequence |
| `array_frequency.py` | Computes a full frequency array for all possible k-mers of length k |
| `pattern.py` | Counts how many times a pattern appears in a text sequence |
| `position.py` | Returns all positions where a pattern occurs in a sequence |
| `number_pattern.py` | Converts a numeric index to its corresponding DNA k-mer |
| `pattern_number.py` | Converts a DNA k-mer to its numeric index |
| `reverse_complement.py` | Returns the reverse complement of a DNA sequence using BioPython |

## Usage

```bash
python side_project.py
# Enter the DNA sequence for nucleotide counting: ATGCGATC
# A is: 2, T is: 2, G is: 2, C is: 2

python frequent_words.py
# Enter a sequence: ACGTTGCATGTCGCATGATGCATGAGAGCT
# Enter a k: 4
# ATGA TGCA

python position.py
# Enter a pattern: ATA
# Enter a sequence: GATATATGCATATACTT
# 1 3 9
```

## Dependencies

```bash
pip install biopython
```
