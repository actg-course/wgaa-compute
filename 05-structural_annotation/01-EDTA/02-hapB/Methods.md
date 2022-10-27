
First, create a symbolic link to our finalized genome assembly FASTA file.  

```bash
ln -s ../../../04-nuclear_assembly/09-renaming/Malus-domestica-WA_38_hapB-genome-v1.0.a1.fa
```

Next, we need the Gala v2 diploid sequences for use with EDTA. We will get those from GDR.
```bash
wget https://www.rosaceae.org/rosaceae_downloads/Malus_x_domestica/Gala_diploid_v1/genes/Gala_diploid_v2.cds.fa.gz
gunzip Gala_diploid_v2.cds.fa.gz
```

Lastly, lanuch EDTA. Note we have to request 10 CPUs in the 
SLURM script because we tell EDTA that it can use 10 threads in the EDTA-hap1.sh script.
```bash
sbatch 01-edta-hapB.srun
```
