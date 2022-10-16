Before we run BUSCO we need access to the final scaffold FASTA file. 
We will create sym links to files we saved after Juicebox curation

```bash
ln -s ../07-juicebox_curation/WA_38-hap1-JBAT.FINAL.fa
ln -s ../07-juicebox_curation/WA_38-hap2-JBAT.FINAL.fa
```

Now run BUSCO on these FASTA files

```bash
sbatch 01-busco-hap1.srun
sbatch 02-busco-hap2.srun
```
