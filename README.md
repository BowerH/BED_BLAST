# Sequence Alignment and Gene Match Tool

This repository includes two Python scripts created for bioinformatics sequence analysis and gene matching using BLAST and BED file data. These were likely developed as part of an academic or research assignment and focus on basic sequence comparison and overlap-based gene hit extraction.

## 🧪 Scripts Overview

### 🔹 `Hbower6_1.py`
A simple sequence comparison script that visually aligns two DNA sequences from a FASTA-like file and highlights matching positions.

#### 🔧 Functionality
- Reads a FASTA-like file containing at least two sequences.
- Compares the sequences character by character.
- Outputs a visual alignment showing matches with `|`.

#### ▶️ Usage

```bash
python Hbower6_1.py input_sequences.txt
```

#### 📄 Input Format
```
>sequence1
ACTGACTG...
>sequence2
ACTAACTC...
```

#### 📤 Output Example
```
ACTGACTG
||| ||||
ACTAACTC
```

### 🔹 Hbower6_EC.py

Parses a BLAST output and a BED annotation file to find genes that align significantly with query sequences based on identity and alignment length thresholds.

#### 🔧 Functionality

Filters BLAST hits by:

Percent identity > 30%

Alignment length > 90% of query length

Matches filtered BLAST hits to genes from a BED file using position overlap and orientation.

Writes gene hits to an output file and prints a match summary.

#### ▶️ Usage
```
python Hbower6_EC.py blast_output.txt genes.bed matched_genes.txt
```

#### 📤 Output Example

Terminal:
```
Matches: geneX
Matches: geneY
Total matches: 2
File (matched_genes.txt):

Match: geneX
Match: geneY

```
## 📦 Requirements

Python 3.x

No external libraries required; uses only built-in Python modules

## 📝 Notes

Make sure the input files are properly formatted:

BLAST file must include query length in the 13th column.

BED file must be tab-delimited with at least 6 columns including orientation.

Sequences in Hbower6_1.py must be of equal length for accurate alignment.

The scripts are primarily intended for educational or prototyping purposes.

## 👩‍💻 Author

Developed by Hannah Bower for coursework in bioinformatics.
