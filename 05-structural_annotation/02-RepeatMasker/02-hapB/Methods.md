# Use RepeatMasker to finalize Repeat Annotation

To infalize our annotations for repeats, we will use the de novo library of TEs that was created using EDTA.
This library will guide RepeatMasker in further identification of repeats as well as add other types of
repeats such as low complexity reagions and simple repeats.

First create a sym link to the TE library created using EDTA.

```bash
ln -s ../../01-EDTA/01-hapB/Malus-domestica-WA_38_hapB-genome-v1.0.a1.fa.mod.EDTA.TElib.fa
```

Next, we also need a sym link to the final genome assembly FASTA file.

```bash
ln -s ../../../04-nuclear_assembly/09-renaming/Malus-domestica-WA_38_hapB-genome-v1.0.a1.fa

Next run RepeatMasker

```bash
sbatch 01-repeatmasker-hapB.srun
```

# Create Masked Files

After RepeatMasker completes we want to create maksed genome FASTA files.  We 
can do this using `bedtools`. First we need togenerate a BED file using the 
output from RepeatMasker. We will use some commnad-line data wrangling tools
to do this.

```bash
sed -e '1,3d' Malus-domestica-WA_38_hapB-genome-v1.0.a1.fa.out | \
  awk -v OFS='\t' '{print $5, $6-1, $7}' | \
  sort -k1,1 -k2,2 -V > Malus-domestica-WA_38_hapB-genome-v1.0.a1.fa.out.bed
```

The BED file can then be used by the bedtools program to create a soft masked 
FASTA file.
```bash
module add singularity
singularity exec -B ${PWD} --no-home docker://systemsgenetics/actg-wgaa-bedtools:2.30.0 \
  bedtools maskfasta \
    -soft \
    -fi Malus-domestica-WA_38_hapB-genome-v1.0.a1.fa \
    -bed Malus-domestica-WA_38_hapB-genome-v1.0.a1.fa.out.bed \
    -fo Malus-domestica-WA_38_hapB-genome-v1.0.a1.softmasked.fa
```

Make a hard-masked file with X's instead of N's.
```bash
singularity exec -B ${PWD} --no-home docker://systemsgenetics/actg-wgaa-bedtools:2.30.0 \
  bedtools maskfasta \
    -mc X \
    -fi Malus-domestica-WA_38_hapB-genome-v1.0.a1.fa \
    -bed Malus-domestica-WA_38_hapB-genome-v1.0.a1.fa.out.bed \
    -fo Malus-domestica-WA_38_hapB-genome-v1.0.a1.Xmasked.fa
```

Create a renamed link for the hard mask that matches the file naming of our other
masked files.
```bash
ln -s Malus-domestica-WA_38_hapB-genome-v1.0.a1.fa.masked Malus-domestica-WA_38_hapB-genome-v1.0.a1.Nmasked.fa
```
