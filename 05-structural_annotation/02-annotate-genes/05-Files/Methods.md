First, this step will use the Python v3 installed on Kamiak. We are not using a Docker image
for this. So, we need to make sure we have the necessary dependencies installed.  We can do that
using an idev session and running the following commands:

```bash
module add python3

pip3 install biopython bcbio-gff
```

The Python script named `generate_structural_files.py` was written sepecifically for this
class and will take the results from TSEBRA (or later Trinity/PASA if we perform it) and
RepeatMasker and generate GFF and FASTA files with features (e.g. genes) properly named
following the naming convenstions, similar to the following:  Maldo.cc.v1a1.chr15A.g000010

With components of the name being:

- Maldo: 5-letter abbreviation for teh genus and species
- cc: 2-letter abbreviation for the cultivar
- v1: The version for the assembly
- a1: The version for the annotation
- chr15A: The chromosome on which the feature is found
- g000010: The gene locus ID.  Genes are numbered in increments of 10.

Transcripts will be given an additional prefix of ".t1" where the number 
increases by incremeents of 1 for each splice variant.

You get get help instructions for running the script by running it with the `-h` flag:
```bash
./generate_structural_files.py -h
```

Create sym links to all the assembly files
```bash
ln -s ../../../04-nuclear_assembly/10-reorient/Malus-domestica-WA_38_hapA-genome-v1.0.a1.fa
ln -s ../../../04-nuclear_assembly/10-reorient/Malus-domestica-WA_38_hapB-genome-v1.0.a1.fa
```

Create sym links to the repeat predictions
```bash
ln -s ../../01-annotate_repeats/02-RepeatMasker/01-hapA/Malus-domestica-WA_38_hapA-genome-v1.0.a1.fa.out
ln -s ../../01-annotate_repeats/02-RepeatMasker/02-hapA/Malus-domestica-WA_38_hapB-genome-v1.0.a1.fa.out
```

Create sym links to the gene predictions
```bash
ln -s ../04-TSEBRA/01-hapA/braker_combined_renamed.gff braker_combined_renamed.hapA.gff
ln -s ../04-TSEBRA/02-hapB/braker_combined_renamed.gff braker_combined_renamed.hapB.gff
```

Now run the scripts for generating the files
```bash
sbatch 01-files_hapA.srun
sbatch 01-files_hapB.srun
```
