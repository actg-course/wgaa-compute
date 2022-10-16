# Misassembly correction

Download the following files to a Windows or Mac computer so that they can be loaded into Juicebox.

* `../06-hic_maps/WA_38-hap1-JBAT.hic`: The Hi-C map file for haplotype #1
* `../06-hic_maps/WA_38-hap2-JBAT.hic`: The Hi-C map file for haplotype #2
* `../06-hic_maps/WA_38-hap1-JBAT.assembly`: An assembly annotation file for Juicebox from haplotype #1
* `../06-hic_maps/WA_38-hap2-JBAT.assembly`: An assembly annotation file for Juicebox from haplotype #2

Misassemblies were explored, and corrected if found, using Juicebox as described in the
[YouTube video](https://www.youtube.com/watch?v=Nj7RhQZHM18). 

The following corrections were made to the scaffolds:

*
* 

Export from Juicebox the updated "assembly" file and "liftover" file and name them (for each haplotype):

* `WA_38-hap1-JBAT.review.assembly`
* `WA_38-hap2-JBAT.review.assembly`
* `WA_38-hap1-JBAT.liftover.agp`
* `WA_38-hap2-JBAT.liftover.agp`

Upload those files to this directory for post processing. 

# Post-processing

Next we need to generate an updated FASTA file of our assembly. We can use the YaHS 
`juicer post` command to do this. Note: YaHS has named its scripts "juicer" in a nod
to compatibility with the Juicer toolset. But this script is not part of Juicer.

First, we will need a sym link to the liftover file from the `juicer pre` command we
ran with YaHS earlier.  

```bash
ln -s ../06-hic_maps/WA_38-hap1-JBAT.liftover.agp
ln -s ../06-hic_maps/WA_38-hap2-JBAT.liftover.agp
```

Second, we need sym links to the original scaffolds FASTA files:
```bash
ln -s ../05-yahs_scaffolding/WA_38.asm.hic.hap1.p_ctg.fa
ln -s ../05-yahs_scaffolding/WA_38.asm.hic.hap2.p_ctg.fa
```

Now we can run the YaHS juicer post command

```bash
sbatch 01-juicer_post-hap1.srun
sbatch 01-juicer_post-hap2.srun
```

