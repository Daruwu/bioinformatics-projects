# Bioinformatics Projects

Python scripts developed during undergraduate bioinformatics coursework, focused on DNA sequence analysis algorithms built from scratch using core Python and BioPython. These tools replicate foundational computational biology techniques used in real genomics pipelines.

**Author:** Darien Nguyen  
**Background:** B.S. Biology | M.S. Data Analytics, Western Governors University  
**Focus:** Applying computational methods to biological sequence data

---

## Repository Structure

```
bioinformatics-projects/
│
├── dna-sequence-analysis/          # Core DNA sequence tools & k-mer analysis
├── approximate-pattern-matching/   # Hamming distance & fuzzy sequence matching
├── kmer-mismatch-analysis/         # k-mer neighborhoods & mismatch-tolerant frequency
├── genome-skew-replication/        # GC skew analysis & replication origin prediction
├── rnaseq-expression-processing/   # DESeq2 output parsing & differential expression
└── gc-content-analysis/            # GC content computation from FASTA files
```

---

## Projects

### 1. DNA Sequence Analysis Toolkit
**[`dna-sequence-analysis/`](./dna-sequence-analysis)**

Core command-line tools for working with raw DNA sequences. Covers nucleotide counting, k-mer frequency computation, pattern matching, positional indexing, and nucleotide-to-number encoding. These are foundational operations used in genome analysis and replication origin detection.

**Tools:** Python, BioPython  
**Key concepts:** k-mer frequency, pattern matching, reverse complement, frequency arrays

---

### 2. Approximate Pattern Matching with Hamming Distance
**[`approximate-pattern-matching/`](./approximate-pattern-matching)**

Implements fuzzy string matching on DNA sequences — finding where a pattern occurs in a genome even when a defined number of mismatches are allowed. Uses Hamming distance as the mismatch metric. Applicable to mutation detection, SNP analysis, and primer design.

**Tools:** Python, BioPython  
**Key concepts:** Hamming distance, approximate matching, mismatch tolerance

---

### 3. k-mer Neighborhood & Mismatch Analysis
**[`kmer-mismatch-analysis/`](./kmer-mismatch-analysis)**

Generates all possible k-mer variants within a given Hamming distance (the "neighborhood") and identifies the most frequent k-mers in a sequence when accounting for mismatches and reverse complements. Used to locate transcription factor binding sites and replication origin candidates.

**Tools:** Python  
**Key concepts:** k-mer neighborhoods, mismatch-tolerant frequency, reverse complement

---

### 4. Genome Skew & Replication Origin Analysis
**[`genome-skew-replication/`](./genome-skew-replication)**

Computes the running GC skew (G minus C count) across a genome and identifies positions where skew is at its minimum — a well-established method for predicting the origin of replication (oriC) in bacterial genomes. Also implements clump finding to detect dense k-mer regions that signal replication hotspots.

**Tools:** Python  
**Key concepts:** GC skew, minimum skew, oriC prediction, clump finding

---

### 5. RNA-seq Differential Expression Data Processing
**[`rnaseq-expression-processing/`](./rnaseq-expression-processing)**

Parses DESeq2 differential expression results alongside sequence annotation data, cross-references gene identifiers between files, filters out NA log-fold change values, and outputs a merged, analysis-ready table. Bridges raw RNA-seq pipeline output and interpretable results for downstream visualization.

**Tools:** Python, NumPy, JSON  
**Key concepts:** DESeq2, differential expression, data merging, tabular processing

---

### 6. GC Content Analysis from FASTA Files
**[`gc-content-analysis/`](./gc-content-analysis)**

Reads multi-record FASTA files, computes GC content for each sequence record using BioPython, and reports the sequence with the highest GC percentage. GC content is a key quality and identity metric in genomics, and this script solves a classic Rosalind bioinformatics problem.

**Tools:** Python, BioPython  
**Key concepts:** GC content, FASTA parsing, sequence quality metrics

---

## Dependencies

```bash
pip install biopython numpy
```

---

## Connect

- **LinkedIn:** [linkedin.com/in/dariennguyen](https://www.linkedin.com/in/dariennguyen)
- **Kaggle:** [kaggle.com/daruwu](https://www.kaggle.com/daruwu)
- **Portfolio:** [daruwu.github.io](https://daruwu.github.io)
- **Email:** darienn9910@gmail.com
