Create symbolic links to the PacBio long reads

```bash
ln -s ../../01-input_data/PacBio/m64233e_211117_203327.fastq.gz .
ln -s ../../01-input_data/PacBio/m64233e_211123_195103.fastq.gz .
```

Run the FastQC slurm job
```bash
sbatch fastqc-pacbio.srun
```

