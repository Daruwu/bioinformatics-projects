# RNA-seq Differential Expression Data Processing

Parses and cross-references DESeq2 differential expression output with sequence annotation files, producing a clean merged table ready for downstream visualization or statistical analysis.

**Why it matters:** RNA-seq pipelines (e.g. Galaxy, DESeq2) output raw tabular results with gene identifiers that often don't match across files. This pipeline merges those results by gene ID, renames keys to strip pipeline-specific prefixes, and filters out genes with NA log-fold change values — turning raw pipeline output into analysis-ready data.

## Scripts

| Script | Description |
|---|---|
| `converttodict.py` | Loads annotation data and DESeq2 results into dictionaries, cross-references by gene ID, and outputs a merged JSON table (`seq_table.txt`) |
| `table2.py` | Extended version — merges annotation with a second DESeq2 result set, filters NA values, and writes a clean tab-delimited output file |

## Input Files Expected

| File | Description |
|---|---|
| `combined.txt` | Sequence annotation file (tab-delimited) |
| `deseq2_G_corn.tabular` | DESeq2 output for condition G |
| `seq2.tabular` | DESeq2 output for a second comparison |

> **Note:** Input file paths in the scripts are set to local paths from development. Update the file paths at the top of each script to match your environment before running.

## Output

- `seq_table.txt` — merged gene expression table with annotation and log-fold change values, NA entries removed

## Dependencies

```bash
pip install numpy
```
