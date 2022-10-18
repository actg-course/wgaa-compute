Before we run BUSCO we need access to the final scaffold FASTA file. 
We will create sym links to files we saved after Juicebox curation. BUSCO
can process each of our haplotypes at the same time if we put them in 
the same directory, so the following code creates a new directory
named `busco_input_files` and creates sym links there.

```bash
mkdir busco_input_files
cd busco_input_files
ln -s ../../07-juicebox_curation/WA_38-hap1-JBAT.FINAL.fa
ln -s ../../07-juicebox_curation/WA_38-hap2-JBAT.FINAL.fa
cd ..

```

Now run BUSCO on these FASTA files

```bash
sbatch busco.srun
```
