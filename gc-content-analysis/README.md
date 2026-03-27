# GC Content Analysis from FASTA Files

Reads a multi-record FASTA file, computes GC content for each sequence, and identifies the record with the highest GC percentage.

**Why it matters:** GC content is a key quality and identity metric in genomics. High GC content indicates greater thermal stability of the double helix. This script solves the classic [Rosalind GC problem](https://rosalind.info/problems/gc/) and is directly applicable to quality control in sequencing workflows.

## Scripts

| Script | Description |
|---|---|
| `transcribe.py` | Parses a FASTA file using BioPython, computes GC% for each record with `SeqUtils.GC`, and prints the record ID and GC percentage of the highest-scoring sequence |

## Usage

```bash
python transcribe.py
# Reads: rosalind_gc.txt (FASTA format)
# Output:
# Rosalind_0808
# 60.919540
```

## Input Format

Standard FASTA file with multiple records:

```
>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
```

## Dependencies

```bash
pip install biopython
```
