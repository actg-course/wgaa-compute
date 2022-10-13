# Step 1: Convert files from YAHS for use by Juicer.

First create links to the YAHS AGP and scaffold files
```bash
ln -s ../05-yahs_scaffolding/WA_38-hap1_scaffolds_final.agp
ln -s ../05-yahs_scaffolding/WA_38-hap2_scaffolds_final.agp
ln -s ../05-yahs_scaffolding/WA_38-hap1_scaffolds_final.fa 
ln -s ../05-yahs_scaffolding/WA_38-hap2_scaffolds_final.fa
```

Create the symlinks for the index FASTA files and their indexes
```bash
ln -s ../05-yahs_scaffolding/WA_38.asm.hic.hap1.p_ctg.fa
ln -s ../05-yahs_scaffolding/WA_38.asm.hic.hap2.p_ctg.fa
ln -s ../05-yahs_scaffolding/WA_38.asm.hic.hap1.p_ctg.fa.fai
ln -s ../05-yahs_scaffolding/WA_38.asm.hic.hap2.p_ctg.fa.fai
```

Create the symlinks for the bin files
```bash
ln -s ../05-yahs_scaffolding/WA_38-hap1.bin 
ln -s ../05-yahs_scaffolding/WA_38-hap2.bin
```

Index the scaffold files
```bash
sbatch 01-samtools-index-hap1.srun
sbatch 02-samtools-index-hap2.srun
```

Create Chromosome sizes files (on a Kamiak idev session)
```bash
cut -f1-2 WA_38-hap1_scaffolds_final.fa.fai > WA_38-hap1_scaffolds_final.chrom.sizes
cut -f1-2 WA_38-hap2_scaffolds_final.fa.fai > WA_38-hap2_scaffolds_final.chrom.sizes
```

Run the YAHS "juicer pre" command.
```bash
03-yahs-juicer-pre-hap1.srun
04-yahs-juicer-pre-hap2.srun
```

# Step 2: Run Juicer to create the HIC files
Instructions for running juicer can be found here: https://github.com/aidenlab/juicer/wiki/Pre

Generate the `.hic` files by running the "juicer_tools pre" command.
```bash
05-juicer_tools-hap1.srun
06-juicer_tools-hap2.srun
```
