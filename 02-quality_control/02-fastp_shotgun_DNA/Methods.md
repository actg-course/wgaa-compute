Create symlinks to the 100X Illumina Shotgun DNA reads

```bash
ln -s ../../01-input_data/Illumina/Shotgun-DNA/JPQN_PCRfree_1_1_GGCTTAAG_Apple_WA38_I1177_L4_R1.fastq.gz
ln -s ../../01-input_data/Illumina/Shotgun-DNA/JPQN_PCRfree_1_1_GGCTTAAG_Apple_WA38_I1177_L4_R2.fastq.gz
```

This trimming step is in preparation for NOVOplasty. That tool specifically states:

> DO NOT filter or quality trim the reads!!! Use the raw whole genome dataset (Only adapters should be removed)!

So, we will instruct fastp to only remove adapters and not trim low quality reads or any
other type of trimming.

Also, fastp can only use 16 threads/cores so we will instruct SLURM to only provide that many.

Run the SLURM script for doing the trimming
```bash
sbatch fastp.srun
```
