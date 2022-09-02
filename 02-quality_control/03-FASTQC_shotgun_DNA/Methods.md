Create symlinks to the 100X Illumina Shotgun DNA reads

```bash
ln -s ../../01-input_data/Illumina/Shotgun-DNA/JPQN_PCRfree_1_1_GGCTTAAG_Apple_WA38_I1177_L4_R1.fastq.gz
ln -s ../../01-input_data/Illumina/Shotgun-DNA/JPQN_PCRfree_1_1_GGCTTAAG_Apple_WA38_I1177_L4_R2.fastq.gz
```

Run the SLURM script for generating the report
```bash
sbatch fastqc.srun
```
