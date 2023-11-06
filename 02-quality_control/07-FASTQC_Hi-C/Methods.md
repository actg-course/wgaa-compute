reate symlinks to the Hi-C DNA reads

```bash
ln -s ../../01-input_data/Illumina/Hi-C/JNQM_OmniC_NA_NA_CTTGTCGA_Apple_Cosmic_Crisp-Apple_WA38_Cosmic_OmniC_I1161L1_L1_R1.fastq
ln -s ../../01-input_data/Illumina/Hi-C/JNQM_OmniC_NA_NA_CTTGTCGA_Apple_Cosmic_Crisp-Apple_WA38_Cosmic_OmniC_I1161L1_L1_R2.fastq
```

Run the SLURM script for generating the report
```bash
sbatch fastqc.srun
```

