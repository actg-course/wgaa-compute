Create symlinks to the 100X Illumina Shotgun DNA reads

```bash
ln -s ../02-fastp_shotgun_DNA/JPQN_PCRfree_1_1_GGCTTAAG_Apple_WA38_I1177_L4_R1.trimmed.fastq.gz
ln -s ../02-fastp_shotgun_DNA/JPQN_PCRfree_1_1_GGCTTAAG_Apple_WA38_I1177_L4_R2.trimmed.fastq.gz
```

Run the SLURM script for generating the report
```bash
sbatch fastqc.srun
```
