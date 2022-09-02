Here we need to run two steps of the Jellyfish software: counting and creation of a histogram. The
results from these steps will be used to import into GenomeScope

First, create sym links to the original data

```bash
ln -s ../../../01-input_data/Illumina/Shotgun-DNA/JPQN_PCRfree_1_1_GGCTTAAG_Apple_WA38_I1177_L4_R1.fastq.gz 
ln -s ../../../01-input_data/Illumina/Shotgun-DNA/JPQN_PCRfree_1_1_GGCTTAAG_Apple_WA38_I1177_L4_R2.fastq.gz 
```

Step 1: Counting
```bash
sbatch 01-jellyfish-count.srun
```

This step generates the `WA38.counts.jf` file

Step 2: Create a histogram
```bash
sbatch 02-jellyfish-histo.srun
```

This step generates the `WA38.counts.histo`
